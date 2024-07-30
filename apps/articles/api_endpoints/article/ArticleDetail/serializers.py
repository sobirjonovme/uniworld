from rest_framework import serializers

from apps.articles.models import Article


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            "id",
            "title",
            "slug",
            "image",
            "content",
            "published_at",
        )
