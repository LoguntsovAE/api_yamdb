import os

from django.contrib.auth.models import send_mail
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from User.models import EmailCode, User
from User.permissions import IsAdmin
from User.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdmin]
    pagination_class = PageNumberPagination
    lookup_field = 'username'

    serializer_class = UserSerializer
    queryset = User.objects.all()


@api_view(['POST'])
def send_email(request):
    data = request.data
    email = data.get('email')
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

    return HttpResponse('<p>Удачно</p>')


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


