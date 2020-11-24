from .base_settings import *
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

if os.getenv('ENV', 'localdev') == 'localdev':
    DEBUG = True
else:
    DEBUG = False

INSTALLED_APPS += [
    # 'rest_framework',
    # 'mdot_rest',
    'django_user_agents',
    'mdot',
    'compressor',
]

MIDDLEWARE += (
    'django.middleware.security.SecurityMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',  
)

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    MEDIA_ROOT = '/app/data/'
    MEDIA_URL = '/media/'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

RESTCLIENTS_MDOT_DAO_CLASS = os.getenv('RESTCLIENTS_MDOT_DAO_CLASS', 'Mock')
RESTCLIENTS_MDOT_HOST = os.getenv('RESTCLIENTS_MDOT_HOST', None)

EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_TIMEOUT = 15
EMAIL_USE_TLS = True
EMAIL_SSL_CERTFILE = os.getenv('CERT_PATH', '')
EMAIL_SSL_KEYFILE = os.getenv('KEY_PATH', '')

MDOT_HELP_EMAIL = os.getenv('MDOT_HELP_EMAIL', 'help@example.edu') # help desk email address
MDOT_SERVICE_EMAIL = os.getenv('MDOT_SERVICE_EMAIL', 'serviceteam@example.edu') # app publishing request email
MDOT_UX_CONTACT = os.getenv('MDOT_UX_CONTACT', '') # String for UX team contact url

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
COMPRESS_ROOT = 'compress_files'

COMPRESS_PRECOMPILERS = (('text/less', 'lesscpy {infile} {outfile}'),)
