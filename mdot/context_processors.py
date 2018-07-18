from django.conf import settings


def less_compiled(request):
    """ See if django-compressor is being used to precompile less
    """
    key = getattr(settings, "COMPRESS_PRECOMPILERS", None)
    return {'less_compiled': key != ()}


def google_analytics(request):

    ga_key = getattr(settings, 'GOOGLE_ANALYTICS_KEY', False)
    return {
        'GOOGLE_ANALYTICS_KEY': ga_key,
        'google_analytics': ga_key
    }


def devtools_bar(request):

    devtools = getattr(settings, 'ACA_DEVTOOLS_ENABLED', False)
    return {
        'devtools_bar': devtools
    }

def get_emails(request):
    help_email = getattr(settings, "MDOT_HELP_EMAIL", None)
    ux_email = getattr(settings, "MDOT_UX_EMAIL", None)
    return {
        "ux_email": ux_email,
        "help_email": help_email
    }
