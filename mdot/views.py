from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.template import RequestContext, Context
from django.shortcuts import render_to_response, render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
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

            params = {
                'service_email': getattr(settings, 'MDOT_SERVICE_EMAIL'),
                'ux_contact': getattr(settings, 'MDOT_UX_CONTACT'),
            }

            email_context = {
                "sponsor_name": "{0} {1}".format(sponsor.first_name, sponsor.last_name),
                "app_name": app.name,
                "agreement_link": "https://mobile.uw.edu/developers/request/{}/".format(app.pk)
            }
            app_requestor_email = '{}@uw.edu'.format(app.requestor.username)
            sponsor_email = "{}@uw.edu".format(sponsor.netid)

            # TODO: send email to sponsor
            try:
                send_mail(
                    'App Sponsorship',
                    get_template("mdot/developers/sponsor_plain_email.html").render(
                        email_context
                    ),
                    app_requestor_email,    # what is this field?
                    [sponsor_email],  # recipients?
                    html_message=get_template(
                        "mdot/developers/sponsor_email.html"
                    ).render(email_context),
                ),
            except BadHeaderError:
                return HttpResponse("Invalid header found.")

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
        return render_to_response('mdot/developers/forbidden.html')

    # check that logged in user is the sponsor
    if app_sponsor.netid == request.user.username:
        # sponsor has agreed
        if request.method == "POST":
            # create agree object
            agreement = Agreement.objects.create(
                app = app
            )
            agreement.save()

            app_manager = app.app_manager
            sponsor_email = "{}@uw.edu".format(app_sponsor.netid)
            email_context = {
                "sponsor_netid": app_sponsor.netid,
                "sponsor_name": "{0} {1}".format(app_sponsor.first_name, app_sponsor.last_name),
                "sponsor_email": sponsor_email,
                "sponsor_dept": app_sponsor.department,
                "sponsor_unit": app_sponsor.unit,
                "manager_name": "{0} {1}".format(app_manager.first_name, app_manager.last_name),
                "manager_netid": app_manager.netid,
                "manager_email": "{}@uw.edu".format(app_manager.netid),
                "app_name": app.name,
                "app_lang": app.primary_language,
                "app_store": list(app.platform.all())
            }

            # TODO: send email to service now
            try:
                send_mail(
                    email_context['sponsor_name'],
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
            agreement = Agreement.objects.filter(app=app, app__app_sponsor__netid=request.user.username)
            if agreement.count() == 0:
                # serve agreement form
                sponsor_name = " ".join((app_sponsor.first_name, app_sponsor.last_name))
                manager_name = " ".join((app.app_manager.first_name, app.app_manager.last_name))
                params = {
                    "app_name": app.name,
                    "manager": manager_name,
                    "sponsor": sponsor_name,
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

    #TODO: render template with correct http code
    return render_to_response("mdot/developers/forbidden.html")
