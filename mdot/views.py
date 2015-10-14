from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response
from htmlmin.decorators import minified_response
from mdot_rest_client.client import MDOT
from dao import pws
import urllib
import json


def home(request):
    params = {'resources': MDOT().get_resources(featured=True)}
    if request.user.is_authenticated():
        params['person'] = pws.get_person_by_netid(request.user.username)
    return render_to_response('mdot/home.html', params,
                              context_instance=RequestContext(request)
                              )
