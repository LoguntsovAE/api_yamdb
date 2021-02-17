from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

# from api_reviews.models.review import Review
# from .permissions import IsAuthorOrReadOnlyPermission
from api_reviews.serializers.review import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticated, IsAuthorOrReadOnlyPermission]
    pass
