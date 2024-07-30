from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from .models import Article, PathwayAdvice


# Register your models here.
class ArticleInline(admin.TabularInline):
    model = Article
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(PathwayAdvice)
class PathwayAdviceAdmin(admin.ModelAdmin):
    list_display = ("id", "_icon", "title", "description")
    search_fields = ("title",)

    def _icon(self, obj):
        return mark_safe(
            '<a href="{url}" target="_blank"><img src="{url}" height="60" />'.format(
                url=obj.icon.url if obj.icon else ""
            )
        )

    _icon.short_description = _("Icon")  # type: ignore
