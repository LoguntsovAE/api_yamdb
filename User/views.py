import os

from django.contrib.auth.models import send_mail
from rest_framework import viewsets
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from User.models import EmailCode, User
from User.permissions import IsAdmin
from User.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]
    pagination_class = PageNumberPagination
    lookup_field = 'username'
    serializer_class = UserSerializer

    @action(methods=['patch', 'get'], detail=False,
            permission_classes=[IsAuthenticated],
            url_path='me', url_name='me')
    def me(self, request, *args, **kwargs):
        instance = self.request.user
        serializer = self.get_serializer(instance)
        if self.request.method == 'PATCH':
            serializer = self.get_serializer(
                instance, data=request.data, partial=True)
            serializer.is_valid()
            serializer.save()
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def send_email(request):
    email = request.data.get('email')
    code = '123456'
    EmailCode.objects.create(
        email=email,
        confirmation_code=code
    )
    send_mail(
        subject='Ваш код авторизации',
        from_email=os.getenv('EMAIL_HOST_DJANGO'),
        recipient_list=[email],
        message=f'Код: {code}'
    )
    return Response('<p>Удачно</p>')


@api_view(['POST'])
def get_token(request):
    data = request.data
    email = data.get('email')
    code = data.get('confirmation_code')
    object_is = EmailCode.objects.filter(
        email=email,
        confirmation_code=code
    ).exists()

    if object_is:
        user = User.objects.create_user(email=email)
        return Response({'token': 'your token'})
    else:
        return Response({'token': 'not'})


