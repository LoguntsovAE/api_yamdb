from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from api_users.views import UserViewSet, send_email, get_token
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenObtainSlidingView
# )


router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet, basename='users')

user = [
    path('email/', send_email, name='email'),
    path('token/', get_token, name='token')
]

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include(user)),
    # path('v1/token/', TokenObtainSlidingView.as_view(), name='token_obtain_pair'),
]

