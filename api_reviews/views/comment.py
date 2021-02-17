from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

# from api_reviews.models.comment import Comment
# from .permissions import IsAuthorOrReadOnlyPermission
from api_reviews.serializers.comment import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    # permission_classes = [IsAuthenticated, IsAuthorOrReadOnlyPermission]
    pass
