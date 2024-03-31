from modeltranslation.translator import TranslationOptions, register

from .models import Country, FrontendTranslation, Region


@register(FrontendTranslation)
class FrontTranslationOptions(TranslationOptions):
    fields = ("text",)


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ("name",)
