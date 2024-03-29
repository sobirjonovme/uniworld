from rest_framework import serializers

from apps.common.serializers import CountrySerializer
from apps.universities.models import University


class UniversityListSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    course_count = serializers.IntegerField(read_only=True, allow_null=True)

    class Meta:
        model = University
        fields = (
            "id",
            "name",
            "logo",
            "is_featured",
            "full_scolarship",
            "country",
            "course_count",
        )
