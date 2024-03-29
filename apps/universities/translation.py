from modeltranslation.translator import TranslationOptions, register

from .models import Specialty, University, UniversityCourse


@register(Specialty)
class SpecialtyTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(University)
class UniversityTranslationOptions(TranslationOptions):
    fields = ("name", "address", "about")


@register(UniversityCourse)
class UniversityCourseTranslationOptions(TranslationOptions):
    fields = ("name",)
