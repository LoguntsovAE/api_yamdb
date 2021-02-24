from rest_framework import serializers

from api_reviews.models.genre import Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre

        exclude = ('pk',)
        lookup_field = 'slug'
