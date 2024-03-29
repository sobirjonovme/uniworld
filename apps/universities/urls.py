from django.urls import path

from .api_endpoints import UniversityDetailAPIView, UniversityListAPIView

app_name = "universities"

urlpatterns = [
    path("list/", UniversityListAPIView.as_view(), name="universities"),
    path("<int:pk>/detail/", UniversityDetailAPIView.as_view(), name="university"),
]
