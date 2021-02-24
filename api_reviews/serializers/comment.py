from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from api_reviews.models.comment import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment

        exclude = ('review',)
