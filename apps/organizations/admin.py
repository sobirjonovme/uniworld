from django.contrib import admin

from .models import Agency


# Register your models here.
@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    pass
