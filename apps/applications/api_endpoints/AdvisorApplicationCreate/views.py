from rest_framework.generics import CreateAPIView

from apps.applications.models import AdvisorApplication

from .serializers import AdvisorApplicationCreateSerializer


class AdvisorApplicationCreateAPIView(CreateAPIView):
    """
    API endpoint that allows to create advisor application.
    <h2> if type is SPEAK_WITH_ADVISOR, request body example:</h2>
    <pre>
    <code>
        {
            "type": "SPEAK_WITH_ADVISOR",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "+998990070101",
            "who_are_you": "STUDENT",
            "country": 1,
            "region": 1
        }
    <br></code>
    </pre>

    <h2> if type is ELIGIBILITY_CHECK, request body example:</h2>
    <pre>
    <code>
        {
            "type": "ELIGIBILITY_CHECK",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "+998990070101",
            "age": 21,
            "current_education_level": "HIGH_SCHOOL",
            "needed_education_level": "BACHELOR",
            "needed_specialty": 5,
            "gpa": "4.2/5.0"
        }
    <br></code>
    </pre>
    """

    queryset = AdvisorApplication.objects.all()
    serializer_class = AdvisorApplicationCreateSerializer


__all__ = ["AdvisorApplicationCreateAPIView"]
