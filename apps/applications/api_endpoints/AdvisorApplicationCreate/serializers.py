from rest_framework import serializers

from apps.applications.models import AdvisorApplication


class AdvisorApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvisorApplication
        fields = (
            "id",
            "first_name",
            "last_name",
            "who_are_you",
            "phone_number",
            "country",
            "region",
        )
        extra_kwargs = {
            "country": {"required": True, "allow_null": False},
            "region": {"required": True, "allow_null": False},
        }
