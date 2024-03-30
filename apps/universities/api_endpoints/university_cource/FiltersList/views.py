from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.universities.choices import QualificationLevels
from apps.universities.models import Specialty, UniversityCourse

from .serializers import SpecialtyListSerializer


class FiltersListAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "university",
                openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="University ID (optional). If passed, only filters for this university will be returned.",
            ),
        ]
    )
    def get(self, request, *args, **kwargs):
        university_id = request.query_params.get("university")
        specialty_qs = Specialty.objects.all().order_by("name")

        if university_id:
            specialty_qs = specialty_qs.filter(courses__university_id=university_id).distinct()
            qualification_levels = (
                UniversityCourse.objects.filter(university_id=university_id)
                .values_list("qualification_level", flat=True)
                .distinct()
            )
        else:
            qualification_levels = [level[0] for level in QualificationLevels.choices]

        data = {
            "qualification_levels": qualification_levels,
            "specialties": SpecialtyListSerializer(specialty_qs, many=True, context={"request": request}).data,
        }

        return Response(data, status=status.HTTP_200_OK)


__all__ = ["FiltersListAPIView"]
