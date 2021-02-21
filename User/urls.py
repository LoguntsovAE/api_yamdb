from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from User.views import SentConfirmCodeView, SentJWTTokenView, UserViewSet

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet, basename='users')


registration = [
    path('email/', SentConfirmCodeView, name='sent_confirm_code'),
    path('token/', SentJWTTokenView, name='sent_jwt_token'),
    path('token/refresh/', TokenRefreshView, name='sent_refresh_token')
]

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include(registration)),
]
