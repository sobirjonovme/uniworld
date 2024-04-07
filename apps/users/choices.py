from django.db import models
from django.utils.translation import gettext_lazy as _


class UserRoles(models.TextChoices):
    ADMIN = "admin", _("Admin")
    AGENCY_OWNER = "agency_owner", _("Agency Owner")
    AGENCY_OPERATOR = "agency_operator", _("Agency Operator")
