from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from apps.universities.filters import UniversityCourseFilter
from apps.universities.models import University, UniversityCourse

from .serializers import UniversityCourseListSerializer


class UniversityCourseListAPIView(ListAPIView):
    queryset = UniversityCourse.objects.all()
    serializer_class = UniversityCourseListSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_class = UniversityCourseFilter

    def get_queryset(self):
        university_slug = self.kwargs.get("slug")
        university = University.objects.filter(slug=university_slug).first()
        return UniversityCourse.objects.filter(university=university).order_by("name")


__all__ = ["UniversityCourseListAPIView"]
