from api_reviews.models.genre import Genre
from api_reviews.models.category import Category
from django.db.models.aggregates import Avg
from rest_framework import serializers

from api_reviews.models.title import Title
from .genre import GenreSerializer
from .category import CategorySerializer


class TitleSerializerGet(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        fields = ('id', 'name', 'year', 'rating', 
                  'description', 'genre', 'category',
            )
        model = Title

    def get_rating(self, obj):
        rating = obj.reviews.all().aggregate(Avg('score')).get('score_avg')
        if rating is None:
            return None
        return rating

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
        fields = ('id', 'name', 'year', 'description',
                  'genre', 'category',
            )
        model = Title

    def get_rating(self, obj):
        rating = obj.reviews.all().aggregate(Avg('score')).get('score_avg')
        if rating is None:
            return 0
        return rating
