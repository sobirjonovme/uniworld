from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.users.models import OperatorCountry, UserRoles

from .choices import ApplicationStatus
from .models import Application


# Register your models here.
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "phone_number", "university", "status_")
    list_display_links = ("id", "first_name", "last_name")
    search_fields = ("first_name", "last_name", "phone_number")
    autocomplete_fields = ("university", "course", "agency", "region")
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

        if user.role == UserRoles.ADMIN:
            return qs

        if user.role == UserRoles.AGENCY_OWNER:
            return qs.filter(agency=user.agency)

        if user.role == UserRoles.AGENCY_OPERATOR:
            operator_country_ids = OperatorCountry.objects.filter(user=user).values_list("country_id", flat=True)
            qs = qs.filter(agency=user.agency, university__country_id__in=operator_country_ids)
            return qs

        # return empty queryset if user has no role
        return qs.none()
