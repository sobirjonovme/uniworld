from rest_framework.generics import ListAPIView

from apps.organizations.models import Agency
from apps.organizations.serializers import AgencyShortSerializer


class AgencyListAPIView(ListAPIView):
    queryset = Agency.objects.all().order_by("name")
    serializer_class = AgencyShortSerializer


__all__ = ["AgencyListAPIView"]
