from rest_framework import serializers

from api_reviews.models.genre import Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre

        fields = ('name', 'slug')
        lookup_field = 'slug'
