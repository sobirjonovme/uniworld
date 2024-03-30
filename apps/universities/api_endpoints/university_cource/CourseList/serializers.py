from rest_framework import serializers

from apps.universities.models import UniversityCourse


class UniversityCourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityCourse
        fields = (
            "id",
            "name",
            "duration",
            "study_type",
            "tuition_fee",
            "intake_months",
        )
