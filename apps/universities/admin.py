from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

from apps.django_admin_inline_paginator.admin import \
    StackedInlinePaginatedMixin
from apps.users.choices import UserRoles

from .models import RequiredDocument, Specialty, University, UniversityCourse


# Register your models here.
class RequiredDocumentInline(admin.TabularInline):
    model = RequiredDocument
    extra = 0


class UniversityCourseInline(StackedInlinePaginatedMixin, TranslationStackedInline):
    model = UniversityCourse
    extra = 0
    ordering = ("-id",)
    per_page = 5


@admin.register(University)
class UniversityAdmin(TranslationAdmin):
    list_display = ("id", "name", "country", "agency", "full_scolarship", "is_featured")
    list_display_links = ("id", "name")
    search_fields = ("name", "name_uz", "name_en", "name_ru")
    list_filter = ("country", "agency", "full_scolarship", "is_featured")
    autocomplete_fields = ("country", "agency")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("-id",)
    inlines = (RequiredDocumentInline, UniversityCourseInline)

    def get_queryset(self, request):
        user = request.user
        qs = super().get_queryset(request)
        qs = qs.select_related("country", "agency")

        if user.is_superuser:
            return qs
        if user.role in [UserRoles.AGENCY_OWNER, UserRoles.AGENCY_OPERATOR]:
            return qs.filter(agency=user.agency)

        return qs.none()


@admin.register(Specialty)
class SpecialtyAdmin(TranslationAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name", "name_uz", "name_en", "name_ru")
    ordering = ("name",)


@admin.register(UniversityCourse)
class UniversityCourseAdmin(TranslationAdmin):
    list_display = ("id", "name", "university", "specialty", "qualification_level", "study_type")
    list_display_links = ("id", "name")
    search_fields = ("name", "name_uz", "name_en", "name_ru")
    list_filter = ("study_type", "qualification_level", "university")
    autocomplete_fields = ("university", "specialty")
    ordering = ("-id",)

    def get_queryset(self, request):
        user = request.user
        qs = super().get_queryset(request)
        qs = qs.select_related("university", "specialty")

        if user.is_superuser:
            return qs

        if user.role in [UserRoles.AGENCY_OWNER, UserRoles.AGENCY_OPERATOR]:
            return qs.filter(university__agency=user.agency)

        return qs
