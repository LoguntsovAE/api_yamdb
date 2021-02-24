from rest_framework import serializers

from api_reviews.models.category import Category
from api_reviews.models.genre import Genre
from api_reviews.models.title import Title

from .category import CategorySerializer
from .genre import GenreSerializer


class TitleSerializerGet(serializers.ModelSerializer):
    rating = serializers.IntegerField()
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Title

        fields = (
            'id', 'name', 'year', 'rating', 'description', 'genre', 'category',
        )


class TitleSerializerPost(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug',
    )

    class Meta:
        model = Title

        fields = (
            'id', 'name', 'year', 'description', 'genre', 'category',
        )
