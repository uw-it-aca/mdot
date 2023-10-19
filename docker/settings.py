from .base_settings import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

ALLOWED_HOSTS += [
    "test.mobile.washington.edu",  # for testing purposes
    "mobile.uw.edu",  # Extraneous after DNS switch
    "m.uw.edu",  # Extraneous after DNS switch unless 301
    "mobile.washington.edu",  # Extraneous after DNS switch unless 301
    "m.washington.edu",  # Extraneous after DNS switch unless 301
]

if os.getenv("ENV", "localdev") == "localdev":
    DEBUG = True
else:
    DEBUG = False
    CSRF_TRUSTED_ORIGINS = [
        f"https://{host}" for host in ALLOWED_HOSTS if host.endswith(".edu")]

GOOGLE_ANALYTICS_KEY = os.getenv('GOOGLE_ANALYTICS_KEY', None)

INSTALLED_APPS += [
    # 'rest_framework',
    # 'mdot_rest',
    "django_user_agents",
    "mdot",
    "compressor",
    # "django.contrib.admin",
]

MIDDLEWARE += (
    "django.middleware.security.SecurityMiddleware",
    "django_user_agents.middleware.UserAgentMiddleware",
    "htmlmin.middleware.HtmlMinifyMiddleware",
    "htmlmin.middleware.MarkRequestMiddleware",
)

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    MEDIA_ROOT = "/app/data/"
    MEDIA_URL = "/media/"
else:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

RESTCLIENTS_MDOT_DAO_CLASS = os.getenv("RESTCLIENTS_MDOT_DAO_CLASS", "Mock")
RESTCLIENTS_MDOT_HOST = os.getenv("RESTCLIENTS_MDOT_HOST", None)
RESTCLIENTS_CA_BUNDLE = '/etc/ssl/certs/ca-certificates.crt'

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = 587
EMAIL_TIMEOUT = 15
EMAIL_USE_TLS = True
EMAIL_SSL_CERTFILE = os.getenv("CERT_PATH", "")
EMAIL_SSL_KEYFILE = os.getenv("KEY_PATH", "")

MDOT_HELP_EMAIL = os.getenv(
    "MDOT_HELP_EMAIL", "help@example.edu"
)  # help desk email address
MDOT_SERVICE_EMAIL = os.getenv(
    "MDOT_SERVICE_EMAIL", "serviceteam@example.edu"
)  # app publishing request email
MDOT_UX_CONTACT = os.getenv("MDOT_UX_CONTACT", "")  # String for UX team contact url

STATICFILES_FINDERS += ("compressor.finders.CompressorFinder",)

TEMPLATES[0]["OPTIONS"]["context_processors"].extend(
    [
        "mdot.context_processors.less_compiled",
        "mdot.context_processors.google_analytics",
        "mdot.context_processors.devtools_bar",
        "mdot.context_processors.get_emails",
    ]
)

# django_compressor
COMPRESS_PRECOMPILERS = (("text/less", "/app/bin/lesscpy {infile} {outfile}"),)

# settings for local development
if os.getenv('AUTH', 'NONE') == 'SAML_MOCK':
    MOCK_SAML_ATTRIBUTES['isMemberOf'] = ['u_test_admin']

# Authentication Groups
ADMIN_AUTHZ_GROUP = os.getenv('ADMIN_AUTHZ_GROUP', 'u_test_admin')

TIME_ZONE = 'America/Los_Angeles'
