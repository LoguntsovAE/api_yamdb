from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from api_reviews.models import Review, Title
from api_reviews.serializers.review import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = []

    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        get_object_or_404(Title, id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user)

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        return title.reviews
