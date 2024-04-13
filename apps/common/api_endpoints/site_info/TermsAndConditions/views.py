from rest_framework.generics import RetrieveAPIView

from apps.common.models import TermsAndConditions

from .serializers import TermsAndConditionsSerializer


class TermsAndConditionsAPIView(RetrieveAPIView):
    serializer_class = TermsAndConditionsSerializer

    def get_object(self):
        return TermsAndConditions.get_solo()


__all__ = ["TermsAndConditionsAPIView"]
