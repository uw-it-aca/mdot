"""
Django settings for local builds.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
from __future__ import absolute_import
import os
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'replaceme-xxxxxxxxxxxxxxxx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += (
    # 'django.contrib.admin',
    # 'django.contrib.messages',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'mdot.context_processors.less_compiled',
                'mdot.context_processors.google_analytics',
                'mdot.context_processors.devtools_bar',
                'mdot.context_processors.get_emails',
            ],
        },
    },
]

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
)

MEDIA_ROOT = ''
MEDIA_URL = '/media/'

# django compressor
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lesscpy {infile} {outfile}'),
    ('text/x-scss', 'django_pyscss.compressor.DjangoScssFilter'),
)
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = False
COMPRESS_OUTPUT_DIR = ''
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter'
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# MDOT RestClient
# RESTCLIENTS_MDOT_DAO_CLASS = 'mdot.mdot_rest_client.client.MDOTLive'
# RESTCLIENTS_MDOT_HOST = 'http://localhost:8000/'

#Emails
MDOT_HELP_EMAIL = 'help@example.edu' # String for help desk email address
MDOT_UX_EMAIL = 'ux@example.edu' # String for UX team email address
MDOT_SERVICE_EMAIL = 'serviceteam@example.edu' # String to email app publishing requests
