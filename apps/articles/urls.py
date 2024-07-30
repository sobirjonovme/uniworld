from django.urls import path

from .api_endpoints import ArticleDetailAPIView

app_name = "articles"

urlpatterns = [
    path("<slug:slug>/detail/", ArticleDetailAPIView.as_view(), name="article-detail"),
]
