from rest_framework import serializers

from api_reviews.models.comment import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Comment
