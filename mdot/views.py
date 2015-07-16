from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response

import urllib
import json

# create your views here

def home(request):
    return render_to_response('mdot/home.html', context_instance=RequestContext(request))

def featured_list(request):
    return render_to_response('mdot/partials/featured_list.html', context_instance=RequestContext(request))
    
def category_list(request):
    return render_to_response('mdot/partials/category_list.html', context_instance=RequestContext(request))

def topic_list(request):
    return render_to_response('mdot/partials/topic_list.html', context_instance=RequestContext(request))
    
def user_profile(request):
    return render_to_response('mdot/partials/user_profile.html', context_instance=RequestContext(request))