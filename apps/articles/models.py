from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField

from apps.common.models import BaseModel


# Create your models here.
class Article(BaseModel):
    title = models.CharField(verbose_name=_("Title"), max_length=255)
    slug = models.SlugField(verbose_name=_("Slug"), max_length=255, unique=True)
    image = ResizedImageField(
        verbose_name=_("Image"),
        upload_to="articles/images/",
        blank=True,
        null=True,
    )
    content = RichTextUploadingField(verbose_name=_("Content"))
    published_at = models.DateTimeField(verbose_name=_("Published at"), default=timezone.now)

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def __str__(self):
        return self.title


class PathwayAdvice(BaseModel):
    title = models.CharField(verbose_name=_("Title"), max_length=255)
    icon = ResizedImageField(
        verbose_name=_("Icon"),
        upload_to="pathway_advices/icons/",
        blank=True,
        null=True,
    )
    description = models.CharField(verbose_name=_("Description"), max_length=255)
    article = models.ForeignKey(
        verbose_name=_("Article"),
        to=Article,
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        verbose_name = _("Pathway Advice")
        verbose_name_plural = _("Pathway Advices")

    def __str__(self):
        return self.title
