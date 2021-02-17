from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

# from api_reviews.models.category import Category
# from .permissions import IsAuthorOrReadOnlyPermission
from api_reviews.serializers.category import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    # permission_classes = [IsAuthenticated, IsAuthorOrReadOnlyPermission]
    pass
