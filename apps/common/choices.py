from django.db import models
from django.utils.translation import gettext_lazy as _


class GenderChoices(models.TextChoices):
    MALE = "male", _("Male")
    FEMALE = "female", _("Female")


class CurrencyChoices(models.TextChoices):
    UZS = "uzs", _("UZS")
    KGS = "kgs", _("KGS")
    KZT = "kzt", _("KZT")
    USD = "usd", _("USD")
    EUR = "eur", _("EUR")
    RUB = "rub", _("RUB")
    KRW = "krw", _("KRW")
    JPY = "jpy", _("JPY")
    CAD = "cad", _("CAD")
    GBP = "gbp", _("GBP")
    MYR = "myr", _("MYR")
    AUD = "aud", _("AUD")
    CNY = "cny", _("CNY")
    SAR = "sar", _("SAR")
    AED = "aed", _("AED")
