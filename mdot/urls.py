from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:

    url(r'^$', 'mdot.views.home', name='home'),
    url(r'^developers/$', 'mdot.views.developers', name='developers'),
    url(r'^developers/guidelines/$', 'mdot.views.guidelines',
        name='guidelines'),
    url(r'^developers/process/$', 'mdot.views.process', name='process'),
    url(r'^developers/review/$', 'mdot.views.review', name='review'),

    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),

    # include applications
    # url(r'^', include('app_name.urls')),
)
