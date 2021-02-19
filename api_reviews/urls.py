from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet)

router_v1 = DefaultRouter()

router_v1.register('titles', TitleViewSet)
router_v1.register('categories', CategoryViewSet)
router_v1.register('genres', GenreViewSet)
router_v1.register('reviews', ReviewViewSet)
router_v1.register('comments', CommentViewSet)
router_v1.register('titles/(?<title_id>\d+)/reviews', ReviewViewSet)
router_v1.register(
    'titles/(?<title_id>\d+)/reviews/(?<review_id>\d+)/comments',
    CommentViewSet
)

urlpatterns = [
    path('v1/', include(router_v1.urls))
]
