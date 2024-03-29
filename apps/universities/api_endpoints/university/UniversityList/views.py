from django.db.models import Count
from rest_framework.generics import ListAPIView

from apps.universities.models import University

from .serializers import UniversityListSerializer


class UniversityListAPIView(ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversityListSerializer

    def get_queryset(self):
        qs = super().get_queryset().order_by("-created_at")
        qs = qs.annotate(
            course_count=Count("courses", distinct=True),
        )
        qs = qs.prefetch_related("country")

        qs = qs.filter(course_count__gt=0)
        return qs


__all__ = ["UniversityListAPIView"]
