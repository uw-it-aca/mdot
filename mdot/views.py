from django.conf import settings
from django.template.loader import get_template
from django.template import RequestContext, Context
from django.shortcuts import render_to_response, render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from htmlmin.decorators import minified_response
from mdot_rest_client.client import MDOT

import urllib
import json
from models import SponsorForm, ManagerForm, AppForm,\
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

# @method_decorator(login_required(), name="dispatch")
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
            # app.requestor = request.user
            app.save()
            appForm.save_m2m()

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

# @login_required
def sponsor(request, pk):
    try:
        app = App.objects.get(pk=pk)
        app_sponsor = app.app_sponsor
    except App.DoesNotExist:
        return render_to_response('mdot/developers/forbidden.html')

    # TODO: check against loggedin user netid
    # temp: checks against 'spon' netid
    sponsor_netid = 'spon'
    user_netid = sponsor_netid
    if app_sponsor.netid == user_netid:
        if request.method == "POST":
            sponsor_agree = request.POST["agree"]
            if sponsor_agree == "true":
                # create agree object
                agreement = Agreement.objects.create(
                    app = app
                )
                agreement.save()

                # TODO: send email to service now
                # try:
                #     send_mail(
                #         sponsor_name,
                #         get_template("mdot/developers/email_plain.html").render(
                #             email_context
                #         ),
                #         sponsor_email,
                #         [getattr(settings, "MDOT_SERVICE_EMAIL", None)],
                #         html_message=get_template(
                #             "mdot/developers/email_html.html"
                #         ).render(email_context),
                #     ),
                # except BadHeaderError:
                #     return HttpResponse("Invalid header found.")

                params = {
                    'service_email': getattr(settings, 'MDOT_SERVICE_EMAIL'),
                    'ux_contact': getattr(settings, 'MDOT_UX_CONTACT'),
                }
                return render_to_response(
                    'mdot/developers/agree.html',
                    params)

            # sponsor declines
            params = {
                "app": app.name
            }
            return render_to_response("mdot/developers/decline.html", params)

        # GET request
        else:
            agreement = Agreement.objects.filter(app=app, app__app_sponsor__netid=sponsor_netid)
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
                    "app_id": pk
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

    return render_to_response("mdot/developers/forbidden.html")
