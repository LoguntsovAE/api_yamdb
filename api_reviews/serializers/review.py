from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api_reviews.models import Title
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

    def validate(self, attrs):
        title = get_object_or_404(
            Title,
            id=self.context['view'].kwargs.get('title_id')
        )
        if (
            self.context['request'].method != 'PATCH'
            and Review.objects.filter(
                title=title,
                author=self.context['request'].user).exists()
        ):
            raise ValidationError('Вы уже писали своё ревью. Хватит!')
        return super().validate(attrs)
