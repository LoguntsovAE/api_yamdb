from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from User.models import User
from api_reviews.serializers.user import UserSerializer
from rest_framework.pagination import PageNumberPagination


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    queryset = User.objects.all()

    def perform_create(self, serializer):
        serializer.save()
