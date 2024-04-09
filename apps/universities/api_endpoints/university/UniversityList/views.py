from django.db.models import Count, OuterRef, Subquery
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

from apps.universities.filters import (UNIVERSITY_COURSE_FILTER_PARAMETERS,
                                       UniversityCourseFilter,
                                       UniversityFilter)
from apps.universities.models import University, UniversityCourse

from .serializers import UniversityListSerializer


class UniversityListAPIView(ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversityListSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = UniversityFilter
    search_fields = ("name", "name_en", "name_uz", "name_ru")

    def get_queryset(self):
        qs = super().get_queryset().order_by("-created_at")
        qs = qs.annotate(
            course_count=Subquery(
                UniversityCourseFilter(
                    self.request.GET, queryset=UniversityCourse.objects.filter(university=OuterRef("id"))
                )
                .qs.values("university")
                .annotate(count=Count("id"))
                .values("count")
            )
        )
        qs = qs.prefetch_related("country")

        qs = qs.filter(course_count__gt=0)
        return qs

    @swagger_auto_schema(manual_parameters=UNIVERSITY_COURSE_FILTER_PARAMETERS)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


__all__ = ["UniversityListAPIView"]
