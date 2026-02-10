from django.urls import path, include
from .models import *
from .views import *
from rest_framework.routers import DefaultRouter
router=DefaultRouter()

router.register(r'video_reaction', VideoReactionViewSet, basename='video_reactions')
router.register(r'video_share', VideoReactionViewSet, basename='video_share')
router.register(r'video_save', VideoReactionViewSet, basename='video_save')
router.register(r'video_download', VideoReactionViewSet, basename='video_download')
router.register(r'video_comment', VideoReactionViewSet, basename='video_comment')
router.register(r'video_view', VideoViewViewSet, basename='video_view')
router.register(r'total_video_views', TotalVideoViewViewSet, basename='total_video_views')
router.register(r'total_video_shares', TotalVideoShareViewSet, basename='total_video_shares')
router.register(r'total_video_reactions', TotalVideoReactionViewSet, basename='total_video_reactions')
router.register(r'total_video_saves', TotalVideoSaveViewSet, basename='total_video_saves')
router.register(r'total_video_downloads', TotalVideoDownloadViewSet, basename='total_video_downloads')
router.register(r'total_video_comments', TotalVideoCommentViewSet, basename='total_video_comments')

router.register(r'post_reaction', PostReactionViewSet, basename='post_reaction')
router.register(r'post_share', PostReactionViewSet, basename='post_share')
router.register(r'post_save', PostReactionViewSet, basename='post_save')
router.register(r'post_comment', PostReactionViewSet, basename='post_comment')
router.register(r'post_view', PostViewViewSet, basename='post_view')
router.register(r'total_post_views', TotalPostViewViewSet, basename='total_post_views')
router.register(r'total_post_reactions', TotalPostReactionViewSet, basename='total_post_reactions')
router.register(r'total_post_shares', TotalPostShareViewSet, basename='total_post_shares')
router.register(r'total_post_saves', TotalPostSaveViewSet, basename='total_post_saves')
router.register(r'total_post_comments', TotalPostCommentViewSet, basename='total_post_comments')

urlpatterns = [
    path('', include(router.urls))
]
