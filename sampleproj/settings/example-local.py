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

# MOCK SAML attributes
MOCK_SAML_ATTRIBUTES = {
    'uwnetid': ['javerage'],
    'affiliations': ['student', 'member'],
    'eppn': ['javerage@washington.edu'],
    'scopedAffiliations': ['student@washington.edu', 'member@washington.edu'],
    'isMemberOf': ['u_test_group', 'u_test_another_group'],
}

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
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# MDOT RestClient
# RESTCLIENTS_MDOT_DAO_CLASS = 'Live'
# RESTCLIENTS_MDOT_HOST = 'http://localhost:8000/'

#Emails
MDOT_HELP_EMAIL = 'help@example.edu' # String for help desk email address
MDOT_UX_CONTACT = 'https://uw.service-now.com/uwc.do?sysparm_direct=true#/catalog_order/3494e9951385a3c0c20bb9004244b073' # String for UX team contact url
MDOT_SERVICE_EMAIL = 'serviceteam@example.edu' # String to email app publishing requests
