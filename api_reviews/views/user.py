from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

# from User.models import User
# from .permissions import IsAuthorOrReadOnlyPermission
from api_reviews.serializers.user import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated, IsAuthorOrReadOnlyPermission]
    pass
