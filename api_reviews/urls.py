from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import category, comment, genre, review, title

router_v1 = DefaultRouter()

router_v1.register('titles', title.TitleViewSet, basename='titles')
router_v1.register('genres', genre.GenreViewSet, basename='genres')
router_v1.register('reviews', review.ReviewViewSet, basename='reviews')
router_v1.register('comments', comment.CommentViewSet, basename='comments')
router_v1.register(
    'categories', category.CategoryViewSet, basename='categories'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews', review.ReviewViewSet,
    basename='review'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    comment.CommentViewSet, basename='comment'
)

urlpatterns = [
    path('v1/', include(router_v1.urls))
]
