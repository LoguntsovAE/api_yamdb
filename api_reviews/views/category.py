from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

from api_reviews.models.category import Category
from api_reviews.permissions import IsAdminOrReadOnly
from api_reviews.serializers.category import CategorySerializer
from api_reviews.viewsets import CreateDestroyReadOnlyCustom


class CategoryViewSet(CreateDestroyReadOnlyCustom):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    permission_classes = [IsAdminOrReadOnly]
    pagination_class = PageNumberPagination
    lookup_field = 'slug'

    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
