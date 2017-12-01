from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls import patterns, include, url, handler404
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from mdot import views
from mdot.views import HomeView

urlpatterns = patterns(
    '',
    # Examples:

    #url(r'^$', 'mdot.views.home', name='home'),
    url(r'^$', HomeView.as_view(template_name="mdot/home.html")),

    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),

    # include applications
    # url(r'^', include('app_name.urls')),
)
