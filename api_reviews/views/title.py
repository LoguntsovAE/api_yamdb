from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

# from api_reviews.models.title import Title
# from .permissions import IsAuthorOrReadOnlyPermission
from api_reviews.serializers.title import TitleSerializerGet, TitleSerializerPost


class TitleViewSet(viewsets.ModelViewSet):
    # serializer_class = TitleSerializer
    # permission_classes = [IsAuthenticated, IsAuthorOrReadOnlyPermission]
    pass
