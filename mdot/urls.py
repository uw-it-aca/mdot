from django.urls import include, path

# from django.contrib import admin
# admin.autodiscover()

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('developers/', views.developers, name='developers'),
    path('developers/guidelines/', views.guidelines,
         name='guidelines'),
    path('developers/process/', views.process, name='process'),
    path('developers/review/', views.review, name='review'),

    # SAML login url
    url(r'^saml/', include('uw_saml.urls')),

    # path('blog/', include('blog.urls')),
    # path('admin/', include(admin.site.urls)),

    # include applications
    # path('', include('app_name.urls')),
]
