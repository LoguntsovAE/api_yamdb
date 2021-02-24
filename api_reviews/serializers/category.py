from rest_framework import serializers

from api_reviews.models.category import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

        exclude = ('id',)
        lookup_field = 'slug'
