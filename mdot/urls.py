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

    # re_path(r'^blog/', include('blog.urls')),
    # re_path(r'^admin/', include(admin.site.urls)),

    # include applications
    # re_path(r'^', include('app_name.urls')),
]
