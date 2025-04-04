from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .api_endpoints import (AboutUsAPIView, CountryListAPIView,
                            FrontendTranslationAPIView, PrivacyPolicyAPIView,
                            RegionListAPIView, TermsAndConditionsAPIView,
                            VersionHistoryAPIView)
from .views import TinyMCEUploadView

app_name = "common"

urlpatterns = [
    # for tinymce in admin panel
    path("tinymce/upload/", csrf_exempt(TinyMCEUploadView.as_view()), name="tinymce_upload"),
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
