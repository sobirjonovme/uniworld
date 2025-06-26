from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_jsonform.models.fields import JSONField

from apps.common.choices import GenderChoices
from apps.common.models import BaseModel

from .choices import (CERTIFICATES_SCHEMA, AdvisorApplicationStatus,
                      AdvisorApplicationType, ApplicationStatus,
                      ContactUsInquiryType, CurrentEducationLevelChoices,
                      NeededEducationLevelChoices, WhoAreYouChoices)


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
    type = models.CharField(
        verbose_name=_("Type"),
        max_length=31,
        choices=AdvisorApplicationType.choices,
    )
    agency = models.ForeignKey(
        verbose_name=_("Agency"), to="organizations.Agency", on_delete=models.SET_NULL, null=True, blank=True
    )
    status = models.CharField(
        verbose_name=_("Status"),
        max_length=15,
        choices=AdvisorApplicationStatus.choices,
        default=AdvisorApplicationStatus.NEW,
    )
    # common fields
    first_name = models.CharField(verbose_name=_("First Name"), max_length=255)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=255)
    phone_number = models.CharField(verbose_name=_("Phone Number"), max_length=31)
    sent_telegram = models.BooleanField(verbose_name=_("Sent Telegram"), default=False)
    # fields for speaking with advisor
    who_are_you = models.CharField(
        verbose_name=_("Who Are You"), max_length=31, choices=WhoAreYouChoices.choices, null=True, blank=True
    )
    country = models.ForeignKey(
        verbose_name=_("Country"), to="common.Country", on_delete=models.SET_NULL, null=True, blank=True
    )
    region = models.ForeignKey(
        verbose_name=_("Region"), to="common.Region", on_delete=models.SET_NULL, null=True, blank=True
    )
    # fields for eligibility check
    age = models.PositiveIntegerField(verbose_name=_("Age"), null=True, blank=True)
    current_education_level = models.CharField(
        verbose_name=_("Current Education Level"),
        max_length=31,
        choices=CurrentEducationLevelChoices.choices,
        null=True,
        blank=True,
    )
    needed_education_level = models.CharField(
        verbose_name=_("Needed Education Level"),
        max_length=31,
        choices=NeededEducationLevelChoices.choices,
        null=True,
        blank=True,
    )
    needed_specialty = models.ForeignKey(
        verbose_name=_("Needed Specialty"),
        to="universities.Specialty",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    gpa = models.CharField(verbose_name=_("GPA"), max_length=63, null=True, blank=True)
    certificates = JSONField(verbose_name=_("Certificates"), schema=CERTIFICATES_SCHEMA, null=True, blank=True)
    matched_universities = models.ManyToManyField(
        verbose_name=_("Matched Universities"), to="universities.University", blank=True
    )

    class Meta:
        verbose_name = _("Request for Advise")
        verbose_name_plural = _("Requests for Advise")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def validate_via_type(self):
        if self.type == AdvisorApplicationType.SPEAK_WITH_ADVISOR:
            required_fields = ["who_are_you", "country", "region"]
        elif self.type == AdvisorApplicationType.ELIGIBILITY_CHECK:
            required_fields = [
                "age",
                "current_education_level",
                "needed_education_level",
                "needed_specialty",
                "gpa",
            ]

        # check if all required fields are filled
        for field in required_fields:
            if not getattr(self, field):
                exception = ValidationError(code="required", message={field: _("This field is required.")})
                setattr(exception, "code", "required")
                raise exception

    def clean(self):
        self.validate_via_type()
        super().clean()


class ContactUsApplication(BaseModel):
    first_name = models.CharField(verbose_name=_("First Name"), max_length=255)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=255)
    telegram_username = models.CharField(verbose_name=_("Telegram Username"), max_length=255)
    phone_number = models.CharField(verbose_name=_("Phone Number"), max_length=31)
    inquiry_type = models.CharField(verbose_name=_("Inquiry Type"), max_length=31, choices=ContactUsInquiryType.choices)
    consulting_agency = models.ForeignKey(
        verbose_name=_("Consulting Agency"), to="organizations.Agency", on_delete=models.SET_NULL, null=True, blank=True
    )
    message = models.TextField(verbose_name=_("Message"))

    class Meta:
        verbose_name = _("Contact Us Application")
        verbose_name_plural = _("Contact Us Applications")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
