from django.urls import path

from .api_endpoints import (
    AboutUsAPIView, CountryListAPIView, FrontendTranslationAPIView, PrivacyPolicyAPIView, RegionListAPIView,
    TermsAndConditionsAPIView, VersionHistoryAPIView
)

app_name = "common"

urlpatterns = [
    # common
    path("countries/", CountryListAPIView.as_view(), name="countries-list"),
    path("regions/", RegionListAPIView.as_view(), name="regions-list"),
    path("FrontendTranslations/", FrontendTranslationAPIView.as_view(), name="frontend-translations"),
    path("VersionHistory/", VersionHistoryAPIView.as_view(), name="version-history"),
    # site info
    path("terms-and-conditions/", TermsAndConditionsAPIView.as_view(), name="terms-and-conditions"),
    path("privacy-policy/", PrivacyPolicyAPIView.as_view(), name="privacy-policy"),
    path("about-us/", AboutUsAPIView.as_view(), name="about-us"),
]
