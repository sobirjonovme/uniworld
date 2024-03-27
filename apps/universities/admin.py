from django.contrib import admin

from .models import University, UniversityCourse, Specialty, RequiredDocument


# Register your models here.
class RequiredDocumentInline(admin.TabularInline):
    model = RequiredDocument
    extra = 0


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    inlines = (RequiredDocumentInline,)


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    pass


@admin.register(UniversityCourse)
class UniversityCourseAdmin(admin.ModelAdmin):
    pass
