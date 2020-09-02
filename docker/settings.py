from .base_settings import *
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

if os.getenv('ENV', "NONE") == 'localdev':
    DEBUG = True
else:
    DEBUG = False

INSTALLED_APPS += [
    # 'rest_framework',
    # 'mdot_rest',
    'django_user_agents',
    'mdot',
    'compressor',
    'uw_saml',
]

MIDDLEWARE += (
    'django_user_agents.middleware.UserAgentMiddleware', 
)

# settings for local development
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    MEDIA_ROOT = '/app/data/'
    MEDIA_URL = '/media/'

STATICFILES_FINDERS += (
    'compressor.finders.CompressorFinder',
)

TEMPLATES[0]['OPTIONS']['context_processors'].extend([
    'mdot.context_processors.less_compiled',
    'mdot.context_processors.google_analytics',
    'mdot.context_processors.devtools_bar',
    'mdot.context_processors.get_emails'
])

# django_compressor
COMPRESS_ROOT = "compress_files"

COMPRESS_PRECOMPILERS = (('text/less', 'lesscpy {infile} {outfile}'),)

#Emails
MDOT_HELP_EMAIL = os.getenv('MDOT_HELP_EMAIL', "help@example.edu") # String for help desk email address
MDOT_UX_CONTACT = os.getenv('MDOT_UX_CONTACT', '') # String for UX team contact url
MDOT_SERVICE_EMAIL = os.getenv('MDOT_SERVICE_EMAIL', 'serviceteam@example.edu') # String to email app publishing requests
