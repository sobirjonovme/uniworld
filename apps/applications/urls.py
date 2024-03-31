from django.urls import path

from .api_endpoints import ApplicationCreateAPIView

app_name = "applications"

urlpatterns = [
    path("create/", ApplicationCreateAPIView.as_view(), name="create"),
]
