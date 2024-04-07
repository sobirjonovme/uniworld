from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.users.choices import UserRoles
from apps.users.models import Operator

from .models import Agency, AgencyCountry


# Register your models here.
class AgencyCountryInline(admin.TabularInline):
    model = AgencyCountry
    extra = 0


class OperatorInline(admin.TabularInline):
    model = Operator
    extra = 0
    fields = (
        "username",
        "first_name",
        "last_name",
        "phone_number",
    )
    show_change_link = True

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone_number", "countries_list")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    ordering = ("-id",)
    inlines = (AgencyCountryInline, OperatorInline)

    def countries_list(self, obj):
        return ", ".join([agency_country.country.name for agency_country in obj.countries.all()])

    countries_list.short_description = _("Countries")  # type: ignore

    def get_queryset(self, request):
        user = request.user
        qs = super().get_queryset(request)

        if user.is_superuser:
            return qs

        if user.role == UserRoles.AGENCY_OWNER:
            return qs.filter(users=user)

        return qs.none()
