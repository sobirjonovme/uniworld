from rest_framework.generics import RetrieveAPIView

from apps.common.models import AboutUs

from .serializers import AboutUsSerializer


class AboutUsAPIView(RetrieveAPIView):
    serializer_class = AboutUsSerializer

    def get_object(self):
        return AboutUs.get_solo()


__all__ = ["AboutUsAPIView"]
