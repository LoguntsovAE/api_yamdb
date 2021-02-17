from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

# from api_reviews.models.genre import Genre
# from .permissions import IsAuthorOrReadOnlyPermission
from api_reviews.serializers.genre import GenreSerializer


class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    # permission_classes = [IsAuthenticated, IsAuthorOrReadOnlyPermission]
    pass
