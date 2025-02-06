from django.urls import path

from .api_endpoints import (AdvisorApplicationCreateAPIView,
                            ApplicationCreateAPIView, ContactUsApplicationCreateAPIView)

app_name = "applications"

urlpatterns = [
    path("create/", ApplicationCreateAPIView.as_view(), name="create"),
    path("contact-us-application/create/", ContactUsApplicationCreateAPIView.as_view(), name="contact-us-application-create"),
    path("advisor-application/create/", AdvisorApplicationCreateAPIView.as_view(), name="advisor-application-create"),
]
