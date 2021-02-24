from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api_reviews.models import Review
from api_reviews.permissions import IsOwnerOrReadOnlyPermission
from api_reviews.serializers.comment import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    permission_classes = [
        IsOwnerOrReadOnlyPermission,
        IsAuthenticatedOrReadOnly
    ]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        review = get_object_or_404(
            Review,
            pk=self.kwargs.get('review_id'),
            title=self.kwargs.get('title_id')
        )

        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review,
            pk=self.kwargs.get('review_id'),
            title=self.kwargs.get('title_id')
        )
        serializer.save(review=review, author=self.request.user)
