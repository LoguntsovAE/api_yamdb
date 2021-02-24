from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api_reviews.models import Title
from api_reviews.permissions import IsOwnerOrReadOnlyPermission
from api_reviews.serializers.review import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    permission_classes = [
        IsOwnerOrReadOnlyPermission,
        IsAuthenticatedOrReadOnly,
    ]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))

        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)
