from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from api_reviews.views import UserViewSet

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router_v1.urls))
]
