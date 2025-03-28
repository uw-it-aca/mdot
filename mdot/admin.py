# Copyright 2025 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.conf import settings
from django.contrib import admin
from .models import *
import logging

from uw_saml.utils import is_member_of_group


admin_group = settings.ADMIN_AUTHZ_GROUP

logger = logging.getLogger("filter")


class SAMLAdminSite(admin.AdminSite):
    def has_permission(self, request):
        return (
            is_member_of_group(request, admin_group) and request.user.is_active
        )

    def __init__(self, *args, **kwargs):
        super(SAMLAdminSite, self).__init__(*args, **kwargs)
        self._registry.update(admin.site._registry)


admin_site = SAMLAdminSite(name="SAMLAdmin")


class PlatformInline(admin.TabularInline):
    model = Platform
    extra = 0


@admin.register(Platform, site=admin_site)
class PlatformAdmin(admin.ModelAdmin):
    model = Platform


class SponsorInLine(admin.TabularInline):
    model = Sponsor
    extra = 0


@admin.register(Sponsor, site=admin_site)
class SponsorAdmin(admin.ModelAdmin):
    model = Sponsor
    list_display = (
        "full_name",
        "netid",
        "department",
    )


class ManagerInLine(admin.TabularInline):
    model = Manager
    extra = 0


@admin.register(Manager, site=admin_site)
class ManagerAdmin(admin.ModelAdmin):
    model = Manager
    list_display = (
        "full_name",
        "netid",
        "email",
    )
    fields = ["first_name", "last_name", "netid", "email"]


# filters agreements into agreed, denied, or pending
class AgreementFilter(admin.SimpleListFilter):
    title = "Agreement"
    parameter_name = "status"

    def lookups(self, request, model_admin):
        return [
            ("agreed", "Agreed"),
            ("pending", "Pending"),
            ("denied", "Denied"),
            ("removed", "Removed"),
        ]

    def queryset(self, request, queryset):
        # make list of app agreements for each status
        agreed_apps, denied_apps, removed_apps = [], [], []
        for app in App.objects.filter(agreement__isnull=False):
            if app.status().startswith("Agreed"):
                agreed_apps.append(app.id)
            elif app.status().startswith("Denied"):
                denied_apps.append(app.id)
            else:  # app.status().startswith('Removed'):
                removed_apps.append(app.id)

        if self.value() == "agreed":
            return queryset.filter(id__in=agreed_apps)

        if self.value() == "denied":
            return queryset.filter(id__in=denied_apps)

        if self.value() == "removed":
            return queryset.filter(id__in=removed_apps)

        if self.value() == "pending":
            return queryset.filter(agreement=None)


class AgreementInLine(admin.TabularInline):
    model = Agreement
    extra = 0
    can_delete = False
    list_display = [
        "__str__",
        "status",
        "agree_time",
        "expiration_date",
    ]
    fields = ["status", "agree_time", "expiration_date"]
    readonly_fields = ["agree_time", "expiration_date"]
    ordering = ["-agree_time"]

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Agreement, site=admin_site)
class AgreementAdmin(admin.ModelAdmin):
    model = Agreement
    date_hierarchy = "agree_time"
    list_display = [
        "__str__",
        "status",
        "agree_time",
        "expiration_date",
    ]
    list_filter = ["app"]


class NoteInLine(admin.TabularInline):
    model = Note
    extra = 0
    list_display = [
        "title",
        "created_on",
    ]
    fields = ["title", "body", "created_on"]
    readonly_fields = ["created_on"]
    ordering = ["-created_on"]

    def has_change_permission(self, request, obj=None):
        return False


class NoteAdmin(admin.ModelAdmin):
    model = Note


class AppInLine(admin.TabularInline):
    model = App
    extra = 0


@admin.register(App, site=admin_site)
class AppAdmin(admin.ModelAdmin):
    inlines = [AgreementInLine, NoteInLine]
    model = App

    list_filter = ("platform", AgreementFilter)
    list_display = (
        "__str__",
        "app_manager",
        "manager_contact",
        "app_sponsor",
        "sponsor_contact",
        "status",
        "platforms",
    )
    fields = [
        "name",
        "primary_language",
        "platform",
        "app_manager",
        "manager_contact",
        "app_sponsor",
        "sponsor_contact",
        "requestor",
        "status",
    ]
    readonly_fields = ["manager_contact", "sponsor_contact", "status"]
