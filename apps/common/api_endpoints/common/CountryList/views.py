from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from apps.common.models import Country
from apps.common.pagination import CountryPagination
from apps.common.serializers import CountrySerializer


class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = CountryPagination

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("is_top",)


__all__ = ["CountryListAPIView"]
