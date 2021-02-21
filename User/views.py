import os

from django.contrib.auth.models import send_mail
from rest_framework import status, views, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.tokens import RefreshToken

from api_yamdb.settings import SIMPLE_JWT
from User.models import User
from User.permissions import IsAdmin
from User.serializers import (EmailSerializer, SentJWTTokenSerializer,
                              UserSerializer)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdmin]
    pagination_class = PageNumberPagination
    lookup_field = 'username'

    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(
        detail=False,
        methods=['get', 'patch'],
        permission_classes=[IsAuthenticated],
    )
    def me(self, request, **kwargs):
        partial = kwargs.pop('partial', True)
        serializer = self.get_serializer(
            request.user,
            data=request.data,
            partial=partial,
        )
        serializer.is_valid()
        self.perform_update(serializer)
        return Response(serializer.data)


def send_confirmation_code(subject, message, recipient):
    send_mail(
        subject=subject,
        message=message,
        from_email=os.getenv('EMAIL_HOST_DJANGO'),
        recipient_list=[recipient]
    )


class SentConfirmCodeView(views.APIView):
    serializer_class = EmailSerializer

    def take_email_sent_confirm(self, user, serializer, token):
        code = token.encode(user.get_payload())
        send_confirmation_code(
            'Alo-Oha! Look mail!'
            f'Your code is: {code}',
            user.email,
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        user = get_object_or_404(User, email=request.data.get('email'))
        token = TokenBackend(
            algorithm=SIMPLE_JWT,
            signing_key=SIMPLE_JWT['SIGNING_KEY'],
        )
        return self.take_email_sent_confirm(user, serializer, token)


class SentJWTTokenView(SentConfirmCodeView):
    serializer_class = SentJWTTokenSerializer

    # Проверка соответствия присланных данных и данных на сервере
    def checking(self, user, serializer, token):
        payload = token.decode(self.request.data.get('confirmation_code'))
        if payload == user.get_payload():
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            },
                status=status.HTTP_200_OK,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
