from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.template import RequestContext, Context
from django.shortcuts import render_to_response, render
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail, EmailMultiAlternatives, BadHeaderError
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from htmlmin.decorators import minified_response
from .mdot_rest_client.client import MDOT

import urllib
import json
from .models import SponsorForm, ManagerForm, AppForm,\
    App, Agreement


def home(request):
    params = {"resources": MDOT().get_resources(featured=True)}
    return render(request, "mdot/home.html", params)


def developers(request):
    return render(request, "mdot/developers/home.html")


def guidelines(request):
    params = {"ux_contact": getattr(settings, "MDOT_UX_CONTACT", None)}
    return render(request, "mdot/developers/guidelines.html", params)


def process(request):
    return render(request, "mdot/developers/process.html")


@login_required
def request(request):
    if request.method == "POST":
        sponsorForm = SponsorForm(request.POST, prefix="sponsor")
        managerForm = ManagerForm(request.POST, prefix="manager")
        appForm = AppForm(request.POST, prefix="app")
        if (sponsorForm.is_valid() and managerForm.is_valid()
                and appForm.is_valid()):
            sponsor = sponsorForm.save()
            manager = managerForm.save()
            app = appForm.save(commit=False)
            app.app_sponsor = sponsor
            app.app_manager = manager
            app.requestor = request.user
            app.save()
            appForm.save_m2m()

            # send email to sponsor
            root_url = request.build_absolute_uri("/").strip("/")
            request_detail_url = reverse("sponsor", args=(app.pk,))

            spon_name = " ".join((sponsor.first_name, sponsor.last_name))
            email_context = {
                "sponsor_name": spon_name,
                "app_name": app.name,
                "agreement_link": "{}{}".format(root_url, request_detail_url)
            }
            app_requestor_email = "{}@uw.edu".format(app.requestor.username)

            msg = EmailMultiAlternatives(
                "App Sponsorship Agreement Required: {}".format(app.name),
                get_template(   # text content
                    "mdot/developers/email/sponsor_plain.html").render(
                    email_context
                ),
                getattr(settings, "MDOT_SERVICE_EMAIL", None),
                [sponsor.email],
                cc=[app_requestor_email]
            )
            msg.attach_alternative(
                get_template(
                    "mdot/developers/email/sponsor.html").render(
                    email_context
                ), "text/html")

            msg.send()

            # send email to service now
            subject = ("MDOT: Mobile Intake Form "
                       "for {} Submitted").format(app.name)
            message = ("The Mobile Intake form has been filled out by {}"
                       " on {}. The details of the submission are included"
                       " below:").format(app.requestor, app.request_date)
            email_service_now(app, subject, message, "incomplete")

            params = {
                "service_email": getattr(settings, "MDOT_SERVICE_EMAIL", None),
                "ux_contact": getattr(settings, "MDOT_UX_CONTACT", None),
            }

            return render_to_response(
                "mdot/developers/thanks.html",
                params)
        else:
            forms = {
                "sponsorform": sponsorForm,
                "managerform": managerForm,
                "appform": appForm,
            }

        # return forms to request page
        return render(request, "mdot/developers/request.html", forms)

    # use prefixes to avoid duplicate field names
    sponsorForm = SponsorForm(prefix="sponsor")
    managerForm = ManagerForm(prefix="manager")
    appForm = AppForm(prefix="app")

    forms = {
        "sponsorform": sponsorForm,
        "managerform": managerForm,
        "appform": appForm,
    }

    # return forms to request page
    return render(request, "mdot/developers/request.html", forms)


@login_required
def sponsor(request, pk):
    try:
        app = App.objects.get(pk=pk)
        app_sponsor = app.app_sponsor
    except App.DoesNotExist:
        raise Http404("App does not exist")

    # check that logged in user is the sponsor
    if app_sponsor.netid != request.user.username:
        raise PermissionDenied()

    # sponsor has agreed
    # check that the sponsor has agreed to all conditions
    if (request.method == "POST"
            and "sponsor-requirements" in request.POST
            and "understand-agreements" in request.POST
            and "understand-manager" in request.POST
            and "agree" in request.POST):
        agreement = Agreement.objects.create(
            app=app
        )
        agreement.save()

        # send email to service now
        spon_name = " ".join((app_sponsor.first_name, app_sponsor.last_name))
        subject = "MDOT: Sponsorship for {} Accepted".format(app.name)
        message = ("The designated app sponsor {0} for the app {1}"
                   " has agreed on {2}.").format(
                       spon_name, app.name, agreement.agree_time)
        email_service_now(app, subject, message, "complete")

        params = {
            'service_email': getattr(settings, "MDOT_SERVICE_EMAIL", None),
            'ux_contact': getattr(settings, "MDOT_UX_CONTACT", None),
        }
        return render_to_response(
            'mdot/developers/agree.html',
            params)

    # GET request
    else:
        agreement = Agreement.objects.filter(
                app=app,
                app__app_sponsor__netid=request.user.username
            )

        if not agreement:
            # serve agreement form
            params = {
                "app_name": app.name,
                "app_id": pk,
                "manager": " ".join(
                    (app.app_manager.first_name, app.app_manager.last_name)),
                "sponsor": " ".join(
                    (app_sponsor.first_name, app_sponsor.last_name)),
                "primary_lang": app.primary_language,
                "platforms": list(app.platform.all()),
                "service_email": getattr(settings, "MDOT_SERVICE_EMAIL", None),
                "ux_contact": getattr(settings, "MDOT_UX_CONTACT", None)
            }
            return render(request, "mdot/developers/sponsor.html", params)
        else:
            # serve thank you page -- sponsor has already agreed to this app
            params = {
                "service_email": getattr(settings, "MDOT_SERVICE_EMAIL", None),
                "ux_contact": getattr(settings, "MDOT_UX_CONTACT", None),
                "app": app.name
            }
            if agreement.latest("agree_time").agree:
                return render_to_response(
                    "mdot/developers/agree.html",
                    params)
            else:
                return render_to_response(
                    "mdot/developers/decline.html",
                    params
                )


@login_required
def decline(request, pk):
    try:
        app = App.objects.get(pk=pk)
        app_sponsor = app.app_sponsor
    except App.DoesNotExist:
        raise Http404("App does not exist")

    if request.user.username != app_sponsor.netid:
        raise PermissionDenied()

    # create new agreement object for app with agree set to false
    agreement = Agreement.objects.filter(
        app=app, app__app_sponsor__netid=request.user.username)
    if not agreement:
        agreement = Agreement.objects.create(
            app=app,
            agree=False
        )
        agreement.save()

        # send email to mdot team and original app requestor
        email_context = {
            "app": app.name,
            "app_sponsor": "{} {}".format(
                app_sponsor.first_name, app_sponsor.last_name)
        }
        app_requestor_email = "{}@uw.edu".format(app.requestor.username)

        # send email to original app requestor and cc service team
        msg = EmailMultiAlternatives(
            "Sponsorship Declined: {}".format(app.name),
            get_template(
                "mdot/developers/email/decline_plain.html"
                ).render(email_context),
            getattr(settings, "MDOT_SERVICE_EMAIL", None),
            [app_requestor_email],
            cc=[getattr(settings, "MDOT_SERVICE_EMAIL", None)]
        )
        msg.attach_alternative(
            get_template(
                "mdot/developers/email/decline.html").render(
                email_context
            ), "text/html")

        msg.send()

    params = {
        "service_email": getattr(settings, "MDOT_SERVICE_EMAIL", None),
        "ux_contact": getattr(settings, "MDOT_UX_CONTACT", None),
        "app": app.name
    }
    return render_to_response("mdot/developers/decline.html", params)


def email_service_now(app, subject, message, status):
    """
    Function that sends an email to the mdot service now team about
    new mobile app requests and any updates
    """
    app_sponsor = app.app_sponsor
    app_manager = app.app_manager
    email_context = {
        "message": message,
        "status": status,
        "sponsor_netid": app_sponsor.netid,
        "sponsor_name": " ".join(
            (app_sponsor.first_name, app_sponsor.last_name)),
        "sponsor_email": app_sponsor.email,
        "sponsor_dept": app_sponsor.department,
        "sponsor_unit": app_sponsor.unit,
        "manager_name": " ".join(
            (app_manager.first_name, app_manager.last_name)),
        "manager_netid": app_manager.netid,
        "manager_email": "{}@uw.edu".format(app_manager.netid),
        "app_name": app.name,
        "app_lang": app.primary_language,
        "app_store": list(app.platform.all())
    }

    try:
        send_mail(
            subject,
            get_template("mdot/developers/email/service_plain.html").render(
                email_context
            ),
            getattr(settings, "MDOT_SERVICE_EMAIL", None),
            [getattr(settings, "MDOT_SERVICE_EMAIL", None)],
            html_message=get_template(
                "mdot/developers/email/service.html"
            ).render(email_context),
        ),
    except BadHeaderError:
        return HttpResponse("Invalid header found.")
