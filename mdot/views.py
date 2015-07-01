from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response

import urllib
import json

# create your views here

def home(request):
    return render_to_response('mdot/home.html', context_instance=RequestContext(request))

def test(request):
    return render_to_response('mdot/test.html', context_instance=RequestContext(request))
