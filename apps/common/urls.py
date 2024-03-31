from django.urls import path

from .api_endpoints import CountryListAPIView, FrontendTranslationAPIView, RegionListAPIView, VersionHistoryAPIView

app_name = "common"

urlpatterns = [
    path("countries/", CountryListAPIView.as_view(), name="countries-list"),
    path("regions/", RegionListAPIView.as_view(), name="regions-list"),
    path("FrontendTranslations/", FrontendTranslationAPIView.as_view(), name="frontend-translations"),
    path("VersionHistory/", VersionHistoryAPIView.as_view(), name="version-history"),
]
