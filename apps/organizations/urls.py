from django.urls import path

from .api_endpoints import *  # noqa

app_name = "organizations"


urlpatterns = [
    path("agency/list/", AgencyListAPIView.as_view(), name="agency-list"),
]