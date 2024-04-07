from typing import List

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from apps.users.models import Operator, OperatorCountry, User, UserRoles


class OperatorCountryInline(admin.TabularInline):
    model = OperatorCountry
    extra = 0


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "id",
        "username",
        "first_name",
        "last_name",
        "role",
        "agency",
    )
    list_display_links = ("id", "username", "first_name", "last_name")
    search_fields = ("id", "username", "first_name", "last_name")
    autocomplete_fields = ("agency",)
    list_filter = ("is_active", "agency", "role")
    ordering = ("-id",)
    inlines = (OperatorCountryInline,)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal info",
            {"fields": ("role", "first_name", "last_name", "agency", "telegram_id", "phone_number", "email")},
        ),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "role",
                    "agency",
                    "telegram_id",
                    "phone_number",
                ),
            },
        ),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.select_related("agency")
        return qs


@admin.register(Operator)
class OperatorAdmin(BaseUserAdmin):
    list_display = (
        "id",
        "username",
        "first_name",
        "last_name",
        "countries_list",
    )
    list_display_links = ("id", "username", "first_name", "last_name")
    list_filter: List[str] = []
    search_fields = ("id", "username", "first_name", "last_name")
    ordering = ("-id",)
    inlines = (OperatorCountryInline,)
    readonly_fields = ("agency", "role", "last_login", "date_joined")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "agency",
                    "role",
                    "first_name",
                    "last_name",
                    "telegram_id",
                    "phone_number",
                    "email",
                    "is_active",
                    "password",
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "telegram_id",
                    "phone_number",
                ),
            },
        ),
    )

    def countries_list(self, obj):
        countries = obj.countries.all()
        if not countries:
            return "—"
        return ", ".join([country.country.name for country in countries])

    countries_list.short_description = "Countries"  # type: ignore

    def save_model(self, request, obj, form, change):
        obj.agency = request.user.agency
        obj.role = UserRoles.AGENCY_OPERATOR
        obj.is_staff = True
        obj.save()

        operator_group = Group.objects.filter(name="Agency Operator").first()
        if not operator_group:
            operator_group = Group.objects.create(name="Agency Operator")
        obj.groups.add(operator_group)

        return obj

    def has_add_permission(self, request):
        if request.user.role == UserRoles.AGENCY_OWNER:
            return True

        return False

    def get_queryset(self, request):
        user = request.user
        qs = super().get_queryset(request)
        qs = qs.prefetch_related("countries__country")

        if user.is_superuser:
            return qs

        if request.user.role == UserRoles.AGENCY_OWNER:
            return qs.filter(agency=request.user.agency)

        return qs.none()
