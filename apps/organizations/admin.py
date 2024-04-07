from django.contrib import admin

from .models import Agency, AgencyCountry


# Register your models here.
class AgencyCountryInline(admin.TabularInline):
    model = AgencyCountry
    extra = 0


@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    ordering = ("-id",)
    inlines = (AgencyCountryInline,)
