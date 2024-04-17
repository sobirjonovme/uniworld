from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.choices import GenderChoices
from apps.common.models import BaseModel

from .choices import ApplicationStatus, WhoAreYouChoices


# Create your models here.
class Application(BaseModel):
    university = models.ForeignKey(
        verbose_name=_("University"), to="universities.University", on_delete=models.SET_NULL, null=True, blank=True
    )
    course = models.ForeignKey(
        verbose_name=_("Course"), to="universities.UniversityCourse", on_delete=models.SET_NULL, null=True, blank=True
    )
    agency = models.ForeignKey(
        verbose_name=_("Agency"), to="organizations.Agency", on_delete=models.SET_NULL, null=True
    )
    operator = models.ForeignKey(
        verbose_name=_("Operator"), to="users.User", on_delete=models.SET_NULL, related_name="applications", null=True
    )
    status = models.CharField(
        verbose_name=_("Status"), max_length=15, choices=ApplicationStatus.choices, default=ApplicationStatus.RECEIVED
    )
    first_name = models.CharField(verbose_name=_("First Name"), max_length=255)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=255)
    age = models.PositiveIntegerField(verbose_name=_("Age"))
    phone_number = models.CharField(verbose_name=_("Phone Number"), max_length=31)
    email = models.EmailField(verbose_name=_("Email"))
    gender = models.CharField(verbose_name=_("Gender"), max_length=15, choices=GenderChoices.choices)
    region = models.ForeignKey(verbose_name=_("Region"), to="common.Region", on_delete=models.SET_NULL, null=True)
    sent_telegram = models.BooleanField(verbose_name=_("Sent Telegram"), default=False)

    class Meta:
        verbose_name = _("Application")
        verbose_name_plural = _("Applications")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class AdvisorApplication(BaseModel):
    agency = models.ForeignKey(
        verbose_name=_("Agency"), to="organizations.Agency", on_delete=models.SET_NULL, null=True, blank=True
    )
    status = models.CharField(
        verbose_name=_("Status"), max_length=15, choices=ApplicationStatus.choices, default=ApplicationStatus.RECEIVED
    )
    first_name = models.CharField(verbose_name=_("First Name"), max_length=255)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=255)
    who_are_you = models.CharField(
        verbose_name=_("Who Are You"), max_length=31, choices=WhoAreYouChoices.choices, null=True
    )
    phone_number = models.CharField(verbose_name=_("Phone Number"), max_length=31)
    country = models.ForeignKey(
        verbose_name=_("Country"), to="common.Country", on_delete=models.SET_NULL, null=True, blank=True
    )
    region = models.ForeignKey(verbose_name=_("Region"), to="common.Region", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _("Advisor Application")
        verbose_name_plural = _("Advisor Applications")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
