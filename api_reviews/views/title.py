from django.db.models import Avg
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from api_reviews.models.title import Title
from api_reviews.permissions import IsAdminOrReadOnly
from api_reviews.serializers.title import (TitleSerializerGet,
                                           TitleSerializerPost)


class TitleFilter(filters.FilterSet):
    genre = filters.CharFilter(field_name='genre__slug')
    category = filters.CharFilter(field_name='category__slug')
    year = filters.CharFilter(field_name='year')
    name = filters.CharFilter(
        field_name='name',
        lookup_expr='contains',
    )

    class Meta:
        model = Title
        fields = (
            'genre', 'category',
            'year', 'name',
        )


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(rating=Avg('reviews__score'))
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = PageNumberPagination
    filter_backends = [filters.DjangoFilterBackend]
    filter = TitleFilter

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'list':
            return TitleSerializerGet
        return TitleSerializerPost
