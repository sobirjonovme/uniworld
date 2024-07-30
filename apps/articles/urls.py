from django.urls import path

from .api_endpoints import ArticleDetailAPIView, PathwayAdviceListAPIView

app_name = "articles"

urlpatterns = [
    # common
    path("pathway-advice/list/", PathwayAdviceListAPIView.as_view(), name="pathway-advice-list"),
    # article
    path("<slug:slug>/detail/", ArticleDetailAPIView.as_view(), name="article-detail"),
]
