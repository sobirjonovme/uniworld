from rest_framework.generics import ListAPIView

from apps.articles.models import PathwayAdvice

from .serializers import PathwayAdviceListSerializer


class PathwayAdviceListAPIView(ListAPIView):
    queryset = PathwayAdvice.objects.all()
    serializer_class = PathwayAdviceListSerializer


__all__ = ["PathwayAdviceListAPIView"]
