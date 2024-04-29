from rest_framework import serializers

from apps.applications.models import AdvisorApplication
from apps.tgbot.services.advice_requests import \
    send_advice_request_info_to_operator


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

    def create(self, validated_data):
        advisor_application = AdvisorApplication(**validated_data)
        advisor_application.save()

        try:
            send_advice_request_info_to_operator(advisor_application)
        except Exception:
            pass

        return advisor_application
