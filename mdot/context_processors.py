# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.conf import settings


def less_compiled(request):
    """See if django-compressor is being used to precompile less"""
    key = getattr(settings, "COMPRESS_PRECOMPILERS", None)
    return {"less_compiled": key != ()}


def google_analytics(request):

    ga_key = getattr(settings, "GOOGLE_ANALYTICS_KEY", False)
    return {"GOOGLE_ANALYTICS_KEY": ga_key, "google_analytics": ga_key}


def devtools_bar(request):

    devtools = getattr(settings, "ACA_DEVTOOLS_ENABLED", False)
    return {"devtools_bar": devtools}


def get_emails(request):
    help_email = getattr(settings, "MDOT_HELP_EMAIL", None)
    ux_contact = getattr(settings, "MDOT_UX_CONTACT", None)
    service_email = getattr(settings, "MDOT_SERVICE_EMAIL", None)
    return {
        "ux_contact": ux_contact,
        "help_email": help_email,
        "service_email": service_email,
    }
