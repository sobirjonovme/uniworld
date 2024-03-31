from django.contrib import admin

from .models import Application


# Register your models here.
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "phone_number", "university")
    list_display_links = ("id", "first_name", "last_name", "phone_number")
    search_fields = ("first_name", "last_name", "phone_number")
    autocomplete_fields = ("university", "course", "agency", "region")
