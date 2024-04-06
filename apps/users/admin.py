from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from apps.users.models import OperatorCountry, User


class OperatorCountryInline(admin.TabularInline):
    model = OperatorCountry
    extra = 0


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "id",
        "username",
        "first_name",
        "last_name",
    )
    list_display_links = ("id", "username", "first_name", "last_name")
    search_fields = ("id", "username", "first_name", "last_name")
    autocomplete_fields = ("agency",)
    list_filter = ("is_active",)
    ordering = ("-id",)
    inlines = (OperatorCountryInline,)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal info",
            {"fields": ("role", "first_name", "last_name", "agency", "telegram_id", "phone_number", "email")},
        ),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "role",
                    "agency",
                    "telegram_id",
                    "phone_number",
                ),
            },
        ),
    )
