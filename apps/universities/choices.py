from django.db import models
from django.utils.translation import gettext_lazy as _


class InstitutionTypes(models.TextChoices):
    PRIVATE = "private", _("Private")
    PUBLIC = "public", _("Public")


class StudyTypes(models.TextChoices):
    FULL_TIME = "full_time", _("Full time")
    PART_TIME = "part_time", _("Part time")
    DISTANCE = "distance", _("Distance")


class QualificationLevels(models.TextChoices):
    FOUNDATION = "foundation", _("Foundation")
    CERTIFICATE = "certificate", _("Certificate")
    BACHELOR = "bachelor", _("Bachelor")
    DIPLOMA = "diploma", _("Diploma")
    MASTER = "master", _("Master")
    UNDERGRADUATE = "undergraduate", _("Undergraduate")
    POSTGRADUATE = "postgraduate", _("Postgraduate")


class RequiredDocumentTypes(models.TextChoices):
    IELTS = "ielts", _("IELTS")
    TOEFL = "toefl", _("TOEFL")


class MonthChoices(models.TextChoices):
    JANUARY = "january", _("January")
    FEBRUARY = "february", _("February")
    MARCH = "march", _("March")
    APRIL = "april", _("April")
    MAY = "may", _("May")
    JUNE = "june", _("June")
    JULY = "july", _("July")
    AUGUST = "august", _("August")
    SEPTEMBER = "september", _("September")
    OCTOBER = "october", _("October")
    NOVEMBER = "november", _("November")
    DECEMBER = "december", _("December")
