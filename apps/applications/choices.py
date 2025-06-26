from django.db import models
from django.utils.translation import gettext_lazy as _


class ApplicationStatus(models.TextChoices):
    RECEIVED = "received", _("Received")
    IN_PROGRESS = "in_progress", _("In Progress")
    FINISHED = "finished", _("Finished")
    CANCELLED = "cancelled", _("Cancelled")


class AdvisorApplicationType(models.TextChoices):
    ELIGIBILITY_CHECK = "eligibility_check", _("Eligibility Check")
    SPEAK_WITH_ADVISOR = "speak_with_advisor", _("Speak with Advisor")


class AdvisorApplicationStatus(models.TextChoices):
    NEW = "new", _("New")
    TALKED = "talked", _("Talked")
    NOT_INTERESTED = "not_interested", _("Not Interested")


class WhoAreYouChoices(models.TextChoices):
    STUDENT = "student", _("Student")
    PARENT = "parent", _("Parent")


class CurrentEducationLevelChoices(models.TextChoices):
    HIGH_SCHOOL = "high_school", _("High School")
    BACHELOR = "bachelor", _("Bachelor")


class NeededEducationLevelChoices(models.TextChoices):
    BACHELOR = "bachelor", _("Bachelor")
    MASTER = "master", _("Master")


class CertificateChoices(models.TextChoices):
    IELTS = "ielts", _("IELTS")
    TOEFL = "toefl", _("TOEFL")
    SAT = "sat", _("SAT")
    GMAT = "gmat", _("GMAT")

    @classmethod
    def get_choices_schema(cls):
        return [{"title": choice.label, "value": choice.value} for choice in cls]


class ContactUsInquiryType(models.TextChoices):
    NEED_HELP = "need_help", _("Need Help")
    COMPLAINT = "complaint", _("Complaint")


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
