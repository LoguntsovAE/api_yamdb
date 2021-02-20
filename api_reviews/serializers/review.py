from rest_framework import serializers

from api_reviews.models.review import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Review
        fields = '__all__'
        extra_kwargs = {'title': {'required': False}}
