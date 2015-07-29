from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response
import urllib
import json


def home(request):
    return render_to_response('mdot/home.html',
                              context_instance=RequestContext(request)
                              )
