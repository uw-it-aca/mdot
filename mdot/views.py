from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response
from mdot_rest_client.client import MDOT
import urllib
import json


def home(request):
    params = {'resources': MDOT().get_resources()}
    return render_to_response('mdot/home.html', params,
                              context_instance=RequestContext(request)
                              )
