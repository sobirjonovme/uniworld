from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.users.models import OperatorCountry, UserRoles

from .choices import ApplicationStatus
from .models import AdvisorApplication, Application


# Register your models here.
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "phone_number", "university", "status_")
    list_display_links = ("id", "first_name", "last_name")
    search_fields = ("first_name", "last_name", "phone_number")
    autocomplete_fields = ("university", "course", "agency", "region", "operator")
    list_filter = ("status",)

    def status_(self, obj):
        status_colors = {
            ApplicationStatus.RECEIVED: "#1fafed",
            ApplicationStatus.IN_PROGRESS: "#3e484f",
            ApplicationStatus.FINISHED: "green",
            ApplicationStatus.CANCELLED: "red",
        }
        return mark_safe(f'<span style="color: {status_colors[obj.status]}"><b>{obj.get_status_display()}</b></span>')

    def get_queryset(self, request):
        user = request.user
        qs = (
            super()
            .get_queryset(request)
            .select_related(
                "university",
            )
        )

        if user.is_superuser:
            return qs

        if user.role == UserRoles.AGENCY_OWNER:
            return qs.filter(agency=user.agency)

        if user.role == UserRoles.AGENCY_OPERATOR:
            operator_country_ids = OperatorCountry.objects.filter(user=user).values_list("country_id", flat=True)
            qs = qs.filter(agency=user.agency, university__country_id__in=operator_country_ids)
            return qs

        # return empty queryset if user has no role
        return qs.none()

    def get_readonly_fields(self, request, obj=None):
        user = request.user
        readonly_fields = list(self.readonly_fields)

        if user.is_superuser:
            return readonly_fields

        if user.role in [UserRoles.AGENCY_OWNER, UserRoles.AGENCY_OPERATOR]:
            extra_readonly_fields = [
                "first_name",
                "last_name",
                "university",
                "course",
                "phone_number",
                "gender",
                "region",
                "age",
                "email",
                "agency",
                "operator",
            ]
            readonly_fields.extend(extra_readonly_fields)

        return readonly_fields


@admin.register(AdvisorApplication)
class AdvisorApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "phone_number", "country", "region", "status_")
    list_display_links = ("id", "first_name", "last_name")
    search_fields = ("first_name", "last_name", "phone_number")
    autocomplete_fields = ("country", "region", "agency")
    list_filter = ("status",)

    def status_(self, obj):
        status_colors = {
            ApplicationStatus.RECEIVED: "#1fafed",
            ApplicationStatus.IN_PROGRESS: "#3e484f",
            ApplicationStatus.FINISHED: "green",
            ApplicationStatus.CANCELLED: "red",
        }
        return mark_safe(f'<span style="color: {status_colors[obj.status]}"><b>{obj.get_status_display()}</b></span>')

    def get_queryset(self, request):
        qs = (
            super()
            .get_queryset(request)
            .select_related(
                "country",
                "region",
            )
        )

        return qs

    def get_readonly_fields(self, request, obj=None):
        user = request.user
        readonly_fields = list(self.readonly_fields)

        if user.is_superuser:
            return readonly_fields

        if user.role in [UserRoles.AGENCY_OWNER, UserRoles.AGENCY_OPERATOR]:
            extra_readonly_fields = [
                "first_name",
                "last_name",
                "who_are_you",
                "phone_number",
                "country",
                "region",
                "agency",
            ]
            readonly_fields.extend(extra_readonly_fields)

        return readonly_fields
