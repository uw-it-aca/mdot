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


@admin.register(Platform, site=admin_site)
class PlatformAdmin(admin.ModelAdmin):
    model = Platform


class PlatformInline(admin.TabularInline):
    model = Platform


@admin.register(Sponsor, site=admin_site)
class SponsorAdmin(admin.ModelAdmin):
    model = Sponsor
    list_display = (
        '__str__',
        'netid',
        'department',
    )


class SponsorInLine(admin.TabularInline):
    model = Sponsor


@admin.register(Manager, site=admin_site)
class ManagerAdmin(admin.ModelAdmin):
    model = Manager
    list_display = (
        '__str__',
        'netid',
        'email',
    )


class ManagerInLine(admin.TabularInline):
    model = Manager


@admin.register(App, site=admin_site)
class AppAdmin(admin.ModelAdmin):
    model = App
    list_display = (
        '__str__',
        'request_date',
    )


class AppInLine(admin.TabularInline):
    model = App


@admin.register(Agreement, site=admin_site)
class AgreementAdmin(admin.ModelAdmin):
    model = Agreement
    list_display = (
        '__str__',
        'agree',
    )


class AgreementInLine(admin.TabularInline):
    model = Agreement
