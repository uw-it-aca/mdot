from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response
from htmlmin.decorators import minified_response
from mdot_rest_client.client import MDOT
import urllib
import json

from django.views.generic.base import TemplateView, TemplateResponse


# home
class HomeView(TemplateView):

    def get_context_data(self, **kwargs):

        # hybrid = self.request.GET.get('h') == 'blah',
        # print hybrid

        context = {
            "resources": MDOT().get_resources(featured=True),
            "hybrid": self.request.GET.get('hybrid') == 'true',
        }
        return context
