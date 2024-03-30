from rest_framework.generics import RetrieveAPIView

from apps.universities.models import University

from .serializers import UniversityDetailSerializer


class UniversityDetailAPIView(RetrieveAPIView):
    queryset = University.objects.all()
    serializer_class = UniversityDetailSerializer
    lookup_field = "slug"
    lookup_url_kwarg = "slug"


__all__ = ["UniversityDetailAPIView"]
