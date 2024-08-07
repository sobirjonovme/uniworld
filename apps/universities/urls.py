from django.urls import path

from .api_endpoints import (FiltersListAPIView, UniversityCourseListAPIView,
                            UniversityDetailAPIView, UniversityListAPIView)

app_name = "universities"

urlpatterns = [
    path("list/", UniversityListAPIView.as_view(), name="university-list"),
    path("<slug:slug>/detail/", UniversityDetailAPIView.as_view(), name="university-detail"),
    path("<slug:slug>/courses/", UniversityCourseListAPIView.as_view(), name="university-courses"),
    path("filters/", FiltersListAPIView.as_view(), name="filters-list"),
]
