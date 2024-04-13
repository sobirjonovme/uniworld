from rest_framework.generics import RetrieveAPIView

from apps.common.models import PrivacyPolicy

from .serializers import PrivacyPolicySerializer


class PrivacyPolicyAPIView(RetrieveAPIView):
    serializer_class = PrivacyPolicySerializer

    def get_object(self):
        return PrivacyPolicy.get_solo()


__all__ = ["PrivacyPolicyAPIView"]
