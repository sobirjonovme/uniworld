from rest_framework.generics import CreateAPIView

from apps.applications.models import AdvisorApplication

from .serializers import AdvisorApplicationCreateSerializer


class AdvisorApplicationCreateAPIView(CreateAPIView):
    """
    API endpoint that allows to create advisor application.
    <h2> if type is speak_with_advisor, request body example:</h2>
    <pre>
    <code>
        {
            "type": "speak_with_advisor",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "+998990070101",
            "who_are_you": "student",
            "country": 1,
            "region": 1
        }
    <br></code>
    </pre>

    <h2> if type is eligibility_check, request body example:</h2>
    <pre>
    <code>
        {
            "type": "eligibility_check",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "+998990070101",
            "age": 21,
            "current_education_level": "high_school",
            "needed_education_level": "bachelor",
            "needed_specialty": 5,
            "gpa": "4.2/5.0"
        }
    <br></code>
    </pre>
    """

    queryset = AdvisorApplication.objects.all()
    serializer_class = AdvisorApplicationCreateSerializer


__all__ = ["AdvisorApplicationCreateAPIView"]
