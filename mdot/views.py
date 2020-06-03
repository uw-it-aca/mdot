from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.template import RequestContext, Context
from django.shortcuts import render_to_response, render
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail, BadHeaderError
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
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
    if request.method == 'POST':
        sponsorForm = SponsorForm(request.POST, prefix='sponsor')
        managerForm = ManagerForm(request.POST, prefix='manager')
        appForm = AppForm(request.POST, prefix='app')
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
            request_detail_url = reverse('request detail', args=(app.pk,))

            email_context = {
                "sponsor_name": " ".join(
                    (sponsor.first_name, sponsor.last_name)),
                "app_name": app.name,
                "agreement_link": "{}{}".format(root_url, request_detail_url)
            }
            app_requestor_email = '{}@uw.edu'.format(app.requestor.username)
            sponsor_email = "{}@uw.edu".format(sponsor.netid)

            try:
                send_mail(
                    'App Sponsorship Agreement Required: {}'.format(app.name),
                    get_template(
                        "mdot/developers/sponsor_plain_email.html").render(
                        email_context
                    ),
                    # TODO: decide on sender email
                    app_requestor_email,
                    [sponsor_email],
                    html_message=get_template(
                        "mdot/developers/sponsor_email.html"
                    ).render(email_context),
                ),
            except BadHeaderError:
                return HttpResponse("Invalid header found.")

            params = {
                'service_email': getattr(settings, 'MDOT_SERVICE_EMAIL'),
                'ux_contact': getattr(settings, 'MDOT_UX_CONTACT'),
            }

            return render_to_response(
                'mdot/developers/thanks.html',
                params)

    else:
        # use prefixes to avoid duplicate field names
        sponsorForm = SponsorForm(prefix='sponsor')
        managerForm = ManagerForm(prefix='manager')
        appForm = AppForm(prefix='app')

    forms = {
        'sponsorform': sponsorForm,
        'managerform': managerForm,
        'appform': appForm,
    }

    # return forms to request page
    return render(request, 'mdot/developers/request.html', forms)


@login_required
def request_detail(request, pk):
    try:
        app = App.objects.get(pk=pk)
        app_sponsor = app.app_sponsor
    except App.DoesNotExist:
        raise Http404("App does not exist")

    # check that logged in user is the sponsor
    if app_sponsor.netid != request.user.username:
        raise PermissionDenied()

    # sponsor has agreed
    if request.method == "POST":
        # create agree object
        agreement = Agreement.objects.create(
            app=app
        )
        agreement.save()

        app_manager = app.app_manager
        sponsor_email = "{}@uw.edu".format(app_sponsor.netid)
        email_context = {
            "sponsor_netid": app_sponsor.netid,
            "sponsor_name": " ".join(
                (app_sponsor.first_name, app_sponsor.last_name)),
            "sponsor_email": sponsor_email,
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
                "Mobile App Request Submitted: {}".format(app.name),
                get_template("mdot/developers/email_plain.html").render(
                    email_context
                ),
                sponsor_email,
                [getattr(settings, "MDOT_SERVICE_EMAIL", None)],
                html_message=get_template(
                    "mdot/developers/email_html.html"
                ).render(email_context),
            ),
        except BadHeaderError:
            return HttpResponse("Invalid header found.")

        params = {
            'service_email': getattr(settings, 'MDOT_SERVICE_EMAIL'),
            'ux_contact': getattr(settings, 'MDOT_UX_CONTACT'),
        }
        return render_to_response(
            'mdot/developers/agree.html',
            params)

    # GET request
    else:
        agreement = Agreement.objects.filter(
            app=app, app__app_sponsor__netid=request.user.username)
        if agreement.count() == 0:
            # serve agreement form
            params = {
                "app_name": app.name,
                "manager": " ".join(
                    (app.app_manager.first_name, app.app_manager.last_name)),
                "sponsor": " ".join(
                    (app_sponsor.first_name, app_sponsor.last_name)),
                "primary_lang": app.primary_language,
                "platforms": list(app.platform.all()),
                "ux_contact": getattr(settings, 'MDOT_UX_CONTACT')
            }
            return render(request, "mdot/developers/sponsor.html", params)
        else:
            # serve thank you page -- sponsor has already agreed to this app
            params = {
                'service_email': getattr(settings, 'MDOT_SERVICE_EMAIL'),
                'ux_contact': getattr(settings, 'MDOT_UX_CONTACT'),
            }
            return render_to_response(
                "mdot/developers/agree.html",
                params)
