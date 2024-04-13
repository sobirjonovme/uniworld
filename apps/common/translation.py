from modeltranslation.translator import TranslationOptions, register

from .models import (AboutUs, Country, FrontendTranslation, PrivacyPolicy,
                     Region, TermsAndConditions)


@register(FrontendTranslation)
class FrontTranslationOptions(TranslationOptions):
    fields = ("text",)


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(TermsAndConditions)
class TermsAndConditionsTranslationOptions(TranslationOptions):
    fields = ("terms",)


@register(PrivacyPolicy)
class PrivacyPolicyTranslationOptions(TranslationOptions):
    fields = ("policy",)


@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ("find_university", "our_services", "card_title", "card_body")
