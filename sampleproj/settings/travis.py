"""
Django settings for travis-ci builds.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
from __future__ import absolute_import
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'travis-xxxxxxxxxxxxxxxx'

#Emails
MDOT_HELP_EMAIL = 'test@testcase.edu' # String for help desk email address
MDOT_UX_EMAIL = 'test@testcase.edu' # String for UX team email address
MDOT_FORM_EMAIL = 'test@testcase.edu' # String to email app publishing requests
