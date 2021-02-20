from rest_framework import serializers

from api_reviews.models.review import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    def validate(self, data):
        """
        проверка на наличие оценки у ревью
        """
        title = self.context.get('title')
        request = self.context.get('request')
        if (
            request.method != 'PATCH' and
            Review.objects.filter(title=title,
                                  author=request.user,
                                  ).exists()):
            raise serializers.ValidationError('Assessment exists!')
        return data

    class Meta:
        model = Review
        fields = '__all__'
        extra_kwargs = {'title': {'required': False}}
