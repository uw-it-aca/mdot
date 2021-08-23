from django.conf import settings
from django.contrib import admin
from .models import *

from uw_saml.utils import is_member_of_group


admin_group = settings.ADMIN_AUTHZ_GROUP

class SAMLAdminSite(admin.AdminSite):
    def has_permission(self, request):
        return (
            is_member_of_group(request, admin_group) and request.user.is_active
        )

    def __init__(self, *args, **kwargs):
        super(SAMLAdminSite, self).__init__(*args, **kwargs)
        self._registry.update(admin.site._registry)


admin_site = SAMLAdminSite(name="SAMLAdmin")
