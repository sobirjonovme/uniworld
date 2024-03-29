from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import RequiredDocument, Specialty, University, UniversityCourse


# Register your models here.
class RequiredDocumentInline(admin.TabularInline):
    model = RequiredDocument
    extra = 0


@admin.register(University)
class UniversityAdmin(TranslationAdmin):
    inlines = (RequiredDocumentInline,)


@admin.register(Specialty)
class SpecialtyAdmin(TranslationAdmin):
    pass


@admin.register(UniversityCourse)
class UniversityCourseAdmin(TranslationAdmin):
    pass
