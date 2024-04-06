from django.contrib import admin

from apps.users.models import OperatorCountry, UserRoles

from .models import Application


# Register your models here.
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "phone_number", "university")
    list_display_links = ("id", "first_name", "last_name", "phone_number")
    search_fields = ("first_name", "last_name", "phone_number")
    autocomplete_fields = ("university", "course", "agency", "region")

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
