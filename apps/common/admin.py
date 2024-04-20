from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from solo.admin import SingletonModelAdmin

from apps.common.mixins import TabbedTranslationMixin
from apps.common.models import (AboutUs, Country, FrontendTranslation,
                                PrivacyPolicy, Region, TermsAndConditions)
from apps.common.views import index_page

# @admin.register(VersionHistory)
# class VersionHistoryAdmin(admin.ModelAdmin):
#     list_display = ("id", "version", "required", "created_at", "updated_at")
#     list_display_links = ("id", "version")
#     list_filter = ("required",)
#     search_fields = ("version",)
#     readonly_fields = ("created_at", "updated_at")


@admin.register(FrontendTranslation)
class FrontTranslationAdmin(TranslationAdmin):
    list_display = ("id", "key", "text", "created_at", "updated_at")
    list_display_links = ("id", "key")
    search_fields = ("key", "text")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Country)
class CountryAdmin(TranslationAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name", "name_uz", "name_en", "name_ru")
    ordering = ("name",)


@admin.register(Region)
class RegionAdmin(TranslationAdmin):
    list_display = (
        "id",
        "name",
    )
    list_display_links = ("id", "name")
    search_fields = ("name", "name_uz", "name_en", "name_ru")
    ordering = ("name",)


@admin.register(TermsAndConditions)
class TermsAndConditionsAdmin(SingletonModelAdmin, TranslationAdmin):
    pass


@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(SingletonModelAdmin, TranslationAdmin):
    pass


@admin.register(AboutUs)
class AboutUsAdmin(TabbedTranslationMixin, SingletonModelAdmin):
    pass


admin.AdminSite.index = index_page
