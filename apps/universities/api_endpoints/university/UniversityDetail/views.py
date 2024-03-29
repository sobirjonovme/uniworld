from rest_framework.generics import RetrieveAPIView

from apps.universities.models import University

from .serializers import UniversityDetailSerializer


class UniversityDetailAPIView(RetrieveAPIView):
    queryset = University.objects.all()
    serializer_class = UniversityDetailSerializer


__all__ = ["UniversityDetailAPIView"]
