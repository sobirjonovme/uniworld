from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.users.models import OperatorCountry, UserRoles

from .choices import (AdvisorApplicationStatus, AdvisorApplicationType,
                      ApplicationStatus)
from .models import AdvisorApplication, Application, ContactUsApplication


# Register your models here.
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "phone_number", "university", "status_", "sent_telegram", "created_at")
    list_display_links = ("id", "first_name", "last_name")
    search_fields = ("first_name", "last_name", "phone_number")
    autocomplete_fields = ("university", "course", "agency", "region", "operator")
    list_filter = ("status", "sent_telegram")
    readonly_fields = ("created_at", "updated_at")

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
    list_display = ("id", "first_name", "last_name", "phone_number", "country", "region", "status_", "sent_telegram", "created_at")
    list_display_links = ("id", "first_name", "last_name")
    search_fields = ("first_name", "last_name", "phone_number")
    autocomplete_fields = ("country", "region", "agency", "needed_specialty")
    list_filter = ("status", "sent_telegram")
    readonly_fields = ("created_at", "updated_at")

    def status_(self, obj):
        status_colors = {
            AdvisorApplicationStatus.NEW: "#1fafed",
            # AdvisorApplicationStatus.TALKED: "#3e484f",
            AdvisorApplicationStatus.TALKED: "green",
            AdvisorApplicationStatus.NOT_INTERESTED: "red",
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

    def get_fields(self, request, obj=None):
        fields = [
            "type",
            "status",
            "first_name",
            "last_name",
            "phone_number",
            "sent_telegram",
            "created_at",
            "updated_at",
        ]

        if obj.type == AdvisorApplicationType.SPEAK_WITH_ADVISOR:
            fields.extend(
                [
                    "who_are_you",
                    "country",
                    "region",
                ]
            )
        elif obj.type == AdvisorApplicationType.ELIGIBILITY_CHECK:
            fields.extend(
                [
                    "age",
                    "current_education_level",
                    "needed_education_level",
                    "needed_specialty",
                    "gpa",
                    "certificates",
                ]
            )

        return fields

    def get_readonly_fields(self, request, obj=None):
        user = request.user
        readonly_fields = list(self.readonly_fields)

        if user.is_superuser:
            return readonly_fields

        if user.role in [UserRoles.AGENCY_OWNER, UserRoles.AGENCY_OPERATOR]:
            extra_readonly_fields = [
                "type",
                "first_name",
                "last_name",
                "who_are_you",
                "phone_number",
                "country",
                "region",
                "agency",
                "age",
                "current_education_level",
                "needed_education_level",
                "needed_specialty",
                "gpa",
            ]
            readonly_fields.extend(extra_readonly_fields)

        return readonly_fields


@admin.register(ContactUsApplication)
class ContactUsApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "phone_number", "inquiry_type", "consulting_agency", "created_at")
    list_display_links = ("id", "first_name", "last_name")
    search_fields = ("first_name", "last_name", "phone_number")
    list_filter = ("inquiry_type", "consulting_agency")
    autocomplete_fields = ("consulting_agency",)
    readonly_fields = ("created_at", "updated_at")
