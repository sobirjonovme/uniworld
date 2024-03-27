from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel, ModifiedArrayField
from .choices import StudyTypes, QualificationLevels, InstitutionTypes, RequiredDocumentTypes, MonthChoices


# Create your models here.
class Specialty(BaseModel):
    name = models.CharField(verbose_name=_("Name"), max_length=255)

    class Meta:
        verbose_name = _("Specialty")
        verbose_name_plural = _("Specialties")

    def __str__(self):
        return self.name


class University(BaseModel):
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    country = models.ForeignKey(
        verbose_name=_("Country"),
        to="common.Country",
        on_delete=models.SET_NULL,
        related_name="universities",
        null=True
    )
    institution_type = models.CharField(
        verbose_name=_("Institution type"), max_length=32, choices=InstitutionTypes.choices
    )
    about = models.TextField(verbose_name=_("About"), blank=True, null=True)
    intake_months = ModifiedArrayField(
        verbose_name=_("Intake month"),
        base_field=models.CharField(max_length=32, choices=MonthChoices.choices),
        null=True,
        blank=True
    )
    # Costs
    tuition_fee = models.CharField(
        verbose_name=_("Tuition fee"), max_length=255, help_text=_("yearly tuition fee"), null=True, blank=True
    )
    application_fee = models.CharField(
        verbose_name=_("Application fee"), max_length=255, null=True, blank=True
    )
    living_cost = models.CharField(
        verbose_name=_("Living cost"), max_length=255, help_text=_("monthly living cost"), null=True, blank=True
    )
    visa_fee = models.CharField(
        verbose_name=_("Visa fee"), max_length=255, null=True, blank=True
    )

    class Meta:
        verbose_name = _("University")
        verbose_name_plural = _("Universities")

    def __str__(self):
        return self.name


class RequiredDocument(BaseModel):
    university = models.ForeignKey(
        verbose_name=_("University"),
        to="universities.University",
        on_delete=models.CASCADE,
        related_name="required_documents"
    )
    document_type = models.CharField(
        verbose_name=_("Document type"), max_length=32, choices=RequiredDocumentTypes.choices
    )
    description = models.CharField(verbose_name=_("Description"), max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = _("Required document")
        verbose_name_plural = _("Required documents")

    def __str__(self):
        return self.get_document_type_display()


class UniversityCourse(BaseModel):
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    university = models.ForeignKey(
        verbose_name=_("University"), to="universities.University", on_delete=models.CASCADE, related_name="courses"
    )
    specialty = models.ForeignKey(
        verbose_name=_("Specialty"),
        to="universities.Specialty",
        on_delete=models.SET_NULL,
        related_name="courses",
        null=True
    )
    qualification_level = models.CharField(
        verbose_name=_("Qualification level"), max_length=32, choices=QualificationLevels.choices
    )
    duration = models.PositiveIntegerField(verbose_name=_("Duration"), help_text=_("In years"))
    study_type = models.CharField(verbose_name=_("Study type"), max_length=32, choices=StudyTypes.choices)
    tuition_fee = models.DecimalField(
        verbose_name=_("Tuition fee"), max_digits=10, decimal_places=2, help_text=_("In USD")
    )
    intake_months = ModifiedArrayField(
        verbose_name=_("Intake month"),
        base_field=models.CharField(max_length=32, choices=MonthChoices.choices),
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _("University course")
        verbose_name_plural = _("University courses")

    def __str__(self):
        return f"{self.university} - {self.specialty}"
