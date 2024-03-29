from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import RequiredDocument, Specialty, University, UniversityCourse


# Register your models here.
class RequiredDocumentInline(admin.TabularInline):
    model = RequiredDocument
    extra = 0


@admin.register(University)
class UniversityAdmin(TranslationAdmin):
    list_display = ("id", "name", "country", "agency", "full_scolarship", "is_featured")
    list_display_links = ("id", "name")
    search_fields = ("name", "name_uz", "name_en", "name_ru")
    list_filter = ("country", "agency", "full_scolarship", "is_featured")
    autocomplete_fields = ("country", "agency")
    ordering = ("-id",)
    inlines = (RequiredDocumentInline,)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.select_related("country", "agency")
        return qs


@admin.register(Specialty)
class SpecialtyAdmin(TranslationAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name", "name_uz", "name_en", "name_ru")


@admin.register(UniversityCourse)
class UniversityCourseAdmin(TranslationAdmin):
    list_display = ("id", "name", "university", "specialty", "qualification_level", "study_type")
    list_display_links = ("id", "name")
    search_fields = ("name", "name_uz", "name_en", "name_ru")
    list_filter = ("study_type", "qualification_level", "university")
    # autocomplete_fields = ("university", "specialty")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.select_related("university", "specialty")
        return qs
