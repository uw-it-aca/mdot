# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.urls import include, path, re_path
from . import views
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from mdot.admin import admin_site

from django.views.generic.base import RedirectView
from mdot.pages import PageView

admin.autodiscover()
admin_site.login = login_required(admin_site.login)

urlpatterns = [
    path('', views.home, name='home'),
    path('developers/', views.developers, name='developers'),
    path('developers/guidelines/', views.guidelines,
         name='guidelines'),
    path('developers/process/', views.process, name='process'),
    path('developers/request/', views.request, name='request'),
    path('developers/request/<int:pk>/', views.sponsor, name='sponsor'),
    path('developers/decline/<int:pk>/', views.decline, name='decline'),

    # path('blog/', include('blog.urls')),
    path('admin/', admin_site.urls),
    
    # temporary vue app location
    re_path('vue/', PageView.as_view(), name="index"),
]
