from modeltranslation.translator import TranslationOptions, register

from .models import Country, FrontendTranslation


@register(FrontendTranslation)
class FrontTranslationOptions(TranslationOptions):
    fields = ("text",)


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ("name",)
