from rest_framework.generics import ListAPIView

from apps.common.models import Region
from apps.common.serializers import RegionSerializer


class RegionListAPIView(ListAPIView):
    queryset = Region.objects.all().order_by("name")
    serializer_class = RegionSerializer


__all__ = ["RegionListAPIView"]
