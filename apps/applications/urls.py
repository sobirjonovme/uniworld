from django.urls import path

from .api_endpoints import (AdvisorApplicationCreateAPIView,
                            ApplicationCreateAPIView)

app_name = "applications"

urlpatterns = [
    path("create/", ApplicationCreateAPIView.as_view(), name="create"),
    path("advisor-application/create/", AdvisorApplicationCreateAPIView.as_view(), name="advisor-application-create"),
]
