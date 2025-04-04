from django.db import models
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField

from apps.common.models import BaseModel


# Create your models here.
class Agency(BaseModel):
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    about = HTMLField(verbose_name=_("About"), blank=True, null=True)
    address = models.CharField(verbose_name=_("Address"), max_length=255, blank=True, null=True)
    phone_number = models.CharField(verbose_name=_("Phone number"), max_length=255, blank=True, null=True)
    email = models.EmailField(verbose_name=_("Email"), max_length=255, blank=True, null=True)
    founded_year = models.CharField(verbose_name=_("Founded year"), max_length=255, blank=True, null=True)
    document = models.FileField(verbose_name=_("Document"), upload_to="documents/", blank=True, null=True)

    class Meta:
        verbose_name = _("Agency")
        verbose_name_plural = _("Agencies")

    def __str__(self):
        return self.name


class AgencyCountry(BaseModel):
    agency = models.ForeignKey(verbose_name=_("Agency"), to=Agency, on_delete=models.CASCADE, related_name="countries")
    country = models.ForeignKey(
        verbose_name=_("Country"), to="common.Country", on_delete=models.CASCADE, related_name="agencies"
    )

    class Meta:
        verbose_name = _("Agency Country")
        verbose_name_plural = _("Agency Countries")
        unique_together = ("agency", "country")

    def __str__(self):
        return f"{self.agency} - {self.country}"
