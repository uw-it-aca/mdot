from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:

    url(r'^$', 'mdotdevs.views.home', name='home'),
    url(r'^guidelines/', 'mdotdevs.views.guidelines', name='guidelines'),
    url(r'^process/', 'mdotdevs.views.process', name='process'),
    url(r'^review/', 'mdotdevs.views.review', name='review'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    # include applications
    # url(r'^', include('app_name.urls')),
)
