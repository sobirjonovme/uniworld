from rest_framework import serializers

from apps.applications.choices import AdvisorApplicationType
from apps.applications.models import AdvisorApplication
from apps.applications.services.matcher import get_matched_universities
from apps.tgbot.services.advice_requests import \
    send_advice_request_info_to_operator
from apps.universities.api_endpoints.university.UniversityList.serializers import \
    UniversityListSerializer


class AdvisorApplicationCreateSerializer(serializers.ModelSerializer):
    matched_universities = UniversityListSerializer(read_only=True, many=True)

    class Meta:
        model = AdvisorApplication
        fields = (
            "id",
            "type",
            "first_name",
            "last_name",
            "phone_number",
            # fields for speaking with advisor
            "who_are_you",
            "country",
            "region",
            # fields for eligibility check
            "age",
            "current_education_level",
            "needed_education_level",
            "needed_specialty",
            "gpa",
            "certificates",
            "matched_universities",
        )

    def validate(self, data):
        advisor_application = AdvisorApplication(**data)
        advisor_application.validate_via_type()

        return data

    def create(self, validated_data):
        advisor_application = AdvisorApplication(**validated_data)
        advisor_application.save()

        if advisor_application.type == AdvisorApplicationType.ELIGIBILITY_CHECK:
            advisor_application.matched_universities.set(get_matched_universities(advisor_application))

        try:
            send_advice_request_info_to_operator(advisor_application)
        except Exception:
            pass

        return advisor_application
