from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


# Create your models here.
class UserRoles(models.TextChoices):
    ADMIN = "admin", _("Admin")
    AGENCY_OWNER = "agency_owner", _("Agency Owner")
    AGENCY_OPERATOR = "agency_operator", _("Agency Operator")


class User(AbstractUser, BaseModel):
    role = models.CharField(_("Role"), max_length=16, choices=UserRoles.choices)
    agency = models.ForeignKey(
        verbose_name=_("Agency"), to="organizations.Agency", on_delete=models.CASCADE, blank=True, null=True
    )
    telegram_id = models.CharField(_("Telegram ID"), max_length=255, blank=True, null=True)
    phone_number = models.CharField(_("Phone Number"), max_length=31, blank=True, null=True)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


class OperatorCountry(BaseModel):
    user = models.ForeignKey(
        verbose_name=_("User"), to="users.User", on_delete=models.CASCADE, related_name="countries"
    )
    country = models.ForeignKey(verbose_name=_("Country"), to="common.Country", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Operator Country")
        verbose_name_plural = _("Operator Countries")
        unique_together = ("user", "country")
