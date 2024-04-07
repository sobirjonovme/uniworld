from django.contrib.auth.models import AbstractUser, Group
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel

from .choices import UserRoles
from .managers import OperatorManager


# Create your models here.
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

    def __str__(self):
        name = f"{self.first_name} {self.last_name}" if self.first_name and self.last_name else self.username
        return name

    def save(self, *args, **kwargs):
        if self.role == [UserRoles.AGENCY_OPERATOR, UserRoles.AGENCY_OWNER, UserRoles.ADMIN]:
            self.is_staff = True
        super().save(*args, **kwargs)

        if self.role == UserRoles.AGENCY_OPERATOR:
            operator_group = Group.objects.filter(name="Agency Operator").first()
            if not operator_group:
                operator_group = Group.objects.create(name="Agency Operator")
            self.groups.add(operator_group)

        if self.role == UserRoles.AGENCY_OWNER:
            self.is_staff = True
            owner_group = Group.objects.filter(name="Agency Owner").first()
            if not owner_group:
                owner_group = Group.objects.create(name="Agency Owner")
            self.groups.add(owner_group)


class OperatorCountry(BaseModel):
    user = models.ForeignKey(
        verbose_name=_("User"), to="users.User", on_delete=models.CASCADE, related_name="countries"
    )
    country = models.ForeignKey(verbose_name=_("Country"), to="common.Country", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Operator Country")
        verbose_name_plural = _("Operator Countries")
        unique_together = ("user", "country")

    def __str__(self):
        return f"{self.user} - {self.country}"

    def clean(self):
        if self.user.role != UserRoles.AGENCY_OPERATOR:
            raise ValidationError({"user": _("User should be operator")})

        agency_country_ids = self.user.agency.countries.values_list("country_id", flat=True)
        if self.country_id not in agency_country_ids:
            raise ValidationError({"country": _("Country should be in agency countries")})


class Operator(User):
    objects = OperatorManager()

    class Meta:
        verbose_name = _("Operator")
        verbose_name_plural = _("Operators")
        proxy = True

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
