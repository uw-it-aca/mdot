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

from django_mobileesp.detector import mobileesp_agent as agent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'replaceme-xxxxxxxxxxxxxxxx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
)

MEDIA_ROOT = ''
MEDIA_URL = '/media/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

COMPRESS_ROOT = ""
COMPRESS_PRECOMPILERS = (('text/less', 'lesscpy {infile} {outfile}'),)
COMPRESS_ENABLED = False  # True if you want to compress your development build
COMPRESS_OFFLINE = False  # True if you want to compress your build offline
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter'
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter',
]

# RESTCLIENTS_MDOT_DAO_CLASS = 'mdot.mdot_rest_client.client.MDOTLive'
RESTCLIENTS_MDOT_HOST = 'http://localhost:8000/'
