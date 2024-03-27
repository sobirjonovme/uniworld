from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


# Create your models here.
class Agency(BaseModel):
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    about = models.TextField(verbose_name=_("About"), blank=True, null=True)

    class Meta:
        verbose_name = _("Agency")
        verbose_name_plural = _("Agencies")

    def __str__(self):
        return self.name
