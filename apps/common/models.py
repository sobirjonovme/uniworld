from django import forms
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel
from tinymce.models import HTMLField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # add updated_at field to update_fields if it is not present
        # so that updated_at field will always be updated
        if update_fields and "updated_at" not in update_fields:
            update_fields.append("updated_at")

        super().save(force_insert, force_update, using, update_fields)


class ModifiedArrayField(ArrayField):
    def formfield(self, **kwargs):
        defaults = {
            "form_class": forms.MultipleChoiceField,
            "choices": self.base_field.choices,
            "widget": forms.CheckboxSelectMultiple,
            **kwargs,
        }
        return super(ArrayField, self).formfield(**defaults)


class VersionHistory(BaseModel):
    version = models.CharField(_("Version"), max_length=64)
    required = models.BooleanField(_("Required"), default=True)

    class Meta:
        verbose_name = _("Version history")
        verbose_name_plural = _("Version histories")

    def __str__(self):
        return self.version


class FrontendTranslation(BaseModel):
    key = models.CharField(_("Key"), max_length=255, unique=True)
    text = models.CharField(_("Text"), max_length=1024)

    class Meta:
        verbose_name = _("Frontend translation")
        verbose_name_plural = _("Frontend translations")

    def __str__(self):
        return str(self.key)


class Country(BaseModel):
    name = models.CharField(_("Name"), max_length=255)
    is_top = models.BooleanField(_("Is top"), default=False)

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def __str__(self):
        return self.name


class Region(BaseModel):
    name = models.CharField(_("Name"), max_length=255)

    class Meta:
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")

    def __str__(self):
        return self.name


class TermsAndConditions(SingletonModel):
    terms = HTMLField(_("Terms and conditions"))

    class Meta:
        verbose_name = _("Terms and conditions")
        verbose_name_plural = _("Terms and conditions")

    def __str__(self):
        return str(_("Terms and conditions"))


class PrivacyPolicy(SingletonModel):
    policy = HTMLField(_("Privacy policy"))

    class Meta:
        verbose_name = _("Privacy policy")
        verbose_name_plural = _("Privacy policy")

    def __str__(self):
        return str(_("Privacy policy"))


class AboutUs(SingletonModel):
    find_university = HTMLField(_("Find the right university"))
    our_services = HTMLField(_("Our services"))
    card_title = models.CharField(_("Card title"), max_length=255, null=True, blank=True)
    card_body = HTMLField(_("Card body"), null=True, blank=True)

    class Meta:
        verbose_name = _("About us")
        verbose_name_plural = _("About us")

    def __str__(self):
        return str(_("About us"))


class SiteSettings(SingletonModel):
    advice_requests_chat_id = models.CharField(
        verbose_name=_("Advice requests Chat ID"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Chat ID in Telegram"),
    )

    class Meta:
        verbose_name = _("Site settings")
        verbose_name_plural = _("Site settings")

    def __str__(self):
        return str(_("Site settings"))
