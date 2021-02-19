from rest_framework import serializers

from api_reviews.models.review import Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'title', 'text', 'pub_date', 'score')
        model = Review
