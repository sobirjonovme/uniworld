from rest_framework import serializers

from apps.articles.models import PathwayAdvice


class PathwayAdviceListSerializer(serializers.ModelSerializer):
    article_slug = serializers.SlugField(source="article.slug")

    class Meta:
        model = PathwayAdvice
        fields = (
            "id",
            "title",
            "article_slug",
            "icon",
            "description",
        )
