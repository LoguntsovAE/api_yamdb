from rest_framework import serializers

from api_reviews.models.title import Title


class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Title