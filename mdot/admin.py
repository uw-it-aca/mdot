from django.conf import settings
from django.contrib import admin
from .models import *

# admin.site.register(App)

class SAMLAdminSite(admin.AdminSite):
    def has_permission(self, request):
        return True

    def __init__(self, *args, **kwargs):
        super(SAMLAdminSite, self).__init__(*args, **kwargs)
        self._registry.update(admin.site._registry)


admin_site = SAMLAdminSite(name="SAMLAdmin")

@admin.register(App, site=admin_site)
class AppAdmin(admin.ModelAdmin):
    model = App
