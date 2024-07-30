from django.utils import timezone
from rest_framework.generics import RetrieveAPIView

from apps.articles.models import Article

from .serializers import ArticleDetailSerializer


class ArticleDetailAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = "slug"
    lookup_url_kwarg = "slug"

    def get_queryset(self):
        now = timezone.now()

        qs = super().get_queryset()
        qs = qs.filter(published_at__lte=now)

        return qs


__all__ = ["ArticleDetailAPIView"]
