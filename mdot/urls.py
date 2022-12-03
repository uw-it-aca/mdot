# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.conf import settings
from django.urls import include, re_path
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from mdot.admin import admin_site
from django.views.generic import TemplateView
from mdot.views.index import home, developers, guidelines, process, request, sponsor, decline
from mdot.views.pages import DefaultPageView

from django.views.generic.base import RedirectView

admin.autodiscover()
admin_site.login = login_required(admin_site.login)

# start with an empty url array
urlpatterns = []

# add debug routes for developing error pages
if settings.DEBUG:
    urlpatterns += [
        re_path(
            r"^500$",
            TemplateView.as_view(template_name="500.html"),
            name="500_response",
        ),
        re_path(
            r"^404$",
            TemplateView.as_view(template_name="404.html"),
            name="404_response",
        ),
    ]


urlpatterns += [
    re_path('django/', home, name='home'),
    re_path('django/developers/', developers, name='developers'),
    re_path('django/developers/guidelines/', guidelines,
         name='guidelines'),
    re_path('django/developers/process/', process, name='process'),

    # sponsor app
    re_path('request', request, name='request'),
    re_path('request/<int:pk>/', sponsor, name='sponsor'),
    re_path('decline/<int:pk>/', decline, name='decline'),

    # path('blog/', include('blog.urls')),
    re_path('admin/', admin_site.urls),
    
    # add api endpoints here

    # add default Vue page routes here
    re_path(r"^(developers|guidelines|process)$", DefaultPageView.as_view()),
    re_path(r"^$", DefaultPageView.as_view()),

    
]
