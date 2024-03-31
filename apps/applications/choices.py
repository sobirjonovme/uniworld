from django.db import models
from django.utils.translation import gettext_lazy as _


class ApplicationStatus(models.TextChoices):
    RECEIVED = "RECEIVED", _("Received")
    IN_PROGRESS = "IN_PROGRESS", _("In Progress")
    FINISHED = "FINISHED", _("Finished")
    CANCELLED = "CANCELLED", _("Cancelled")
