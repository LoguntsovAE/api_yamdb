from rest_framework import serializers

from api_reviews.models.genre import Genre


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Genre
