from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from core.swagger.schema import swagger_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("api/v1/common/", include("apps.common.urls")),
    path("api/v1/organizations/", include("apps.organizations.urls")),
    path("api/v1/universities/", include("apps.universities.urls")),
    path("api/v1/applications/", include("apps.applications.urls")),
    path("api/v1/article/", include("apps.articles.urls")),
    path("api/v1/bot/", include("apps.tgbot.urls")),
]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
