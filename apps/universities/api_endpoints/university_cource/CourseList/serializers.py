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
            "qualification_level",
            "tuition_fee",
            "tuition_fee_currency",
            "intake_months",
        )
