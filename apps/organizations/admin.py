from django.contrib import admin

from .models import Agency


# Register your models here.
@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    ordering = ("-id",)
