from django.urls import include, path
from . import views
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from mdot.admin import admin_site

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

    # include applications
    # path('', include('app_name.urls')),
]
