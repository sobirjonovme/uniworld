from django.db import models
from django.utils.translation import gettext_lazy as _


class ApplicationStatus(models.TextChoices):
    RECEIVED = "RECEIVED", _("Received")
    IN_PROGRESS = "IN_PROGRESS", _("In Progress")
    FINISHED = "FINISHED", _("Finished")
    CANCELLED = "CANCELLED", _("Cancelled")


class AdvisorApplicationType(models.TextChoices):
    ELIGIBILITY_CHECK = "ELIGIBILITY_CHECK", _("Eligibility Check")
    SPEAK_WITH_ADVISOR = "SPEAK_WITH_ADVISOR", _("Speak with Advisor")


class AdvisorApplicationStatus(models.TextChoices):
    NEW = "NEW", _("New")
    TALKED = "TALKED", _("Talked")
    NOT_INTERESTED = "NOT_INTERESTED", _("Not Interested")


class WhoAreYouChoices(models.TextChoices):
    STUDENT = "STUDENT", _("Student")
    PARENT = "PARENT", _("Parent")


class CurrentEducationLevelChoices(models.TextChoices):
    HIGH_SCHOOL = "HIGH_SCHOOL", _("High School")
    BACHELOR = "BACHELOR", _("Bachelor")


class NeededEducationLevelChoices(models.TextChoices):
    BACHELOR = "BACHELOR", _("Bachelor")
    MASTER = "MASTER", _("Master")


class CertificateChoices(models.TextChoices):
    IELTS = "IELTS", _("IELTS")
    TOEFL = "TOEFL", _("TOEFL")
    SAT = "SAT", _("SAT")
    GMAT = "GMAT", _("GMAT")

    @classmethod
    def get_choices_schema(cls):
        return [{"title": choice.label, "value": choice.value} for choice in cls]


CERTIFICATES_SCHEMA = {
    "type": "list",
    "items": {
        "type": "dict",
        "keys": {
            "certificate": {"type": "string", "choices": CertificateChoices.get_choices_schema()},
            "score": {"type": "number"},
        },
    },
}
