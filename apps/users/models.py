from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


# Create your models here.
class UserRoles(models.TextChoices):
    ADMIN = "admin", _("Admin")


class User(AbstractUser, BaseModel):
    role = models.CharField(_("Role"), max_length=16, choices=UserRoles.choices)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
