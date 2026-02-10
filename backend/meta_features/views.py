from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from django.db.models import Count
from django.http import JsonResponse
# Create your views here.

class VideoReactionViewSet(viewsets.ModelViewSet):
    queryset=VideoReaction.objects.all()
    serializer_class=VideoReactionSerializer
    http_method_names=['get','post','delete']

class VideoShareViewSet(viewsets.ModelViewSet):
    queryset=VideoShare.objects.all()
    serializer_class=VideoShareSerializer
    http_method_names=['get','post']

class VideoSaveViewSet(viewsets.ModelViewSet):
    queryset=VideoSave.objects.all()
    serializer_class=VideoSaveSerializer
    http_method_names=['get','post','delete']

class VideoDownloadViewSet(viewsets.ModelViewSet):
    queryset=VideoDownload.objects.all()
    serializer_class=VideoDownloadSerializer
    http_method_names=['get','post']

class VideoCommentViewSet(viewsets.ModelViewSet):
    queryset=VideoComment.objects.all()
    serializer_class=VideoCommentSerializer
    http_method_names=['get','post']
    
class VideoViewViewSet(viewsets.ModelViewSet):
    queryset=VideoView.objects.all()
    serializer_class=VideoViewSerializer
    http_method_names=['get','post']


class TotalVideoViewViewSet(viewsets.ReadOnlyModelViewSet):
    # def list(self, request):
    #     total_views=VideoView.objects.count()
    #     return JsonResponse({'total_video_views':total_views})

    queryset=(VideoView.objects.values('video').annotate(total_views=Count('id')))
    serializer_class=TotalVideoViewSerializer
    http_method_names=['get']

class TotalVideoReactionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=(VideoReaction.objects.values('video').annotate(total_reactions=Count('id')))
    serializer_class=TotalVideoReactionSerializer
    http_method_names=['get']
class TotalVideoShareViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=(VideoShare.objects.values('video').annotate(total_shares=Count('id')))
    serializer_class=TotalVideoShareSerializer
    http_method_names=['get']
class TotalVideoSaveViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=(VideoSave.objects.values('video').annotate(total_saves=Count('id')))
    serializer_class=TotalVideoSaveSerializer
    http_method_names=['get']
class TotalVideoDownloadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=(VideoDownload.objects.values('video').annotate(total_downloads=Count('id')))
    serializer_class=TotalVideoDownloadSerializer
    http_method_names=['get']
class TotalVideoCommentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=(VideoComment.objects.values('video').annotate(total_comments=Count('id')))
    serializer_class=TotalVideoCommentSerializer
    http_method_names=['get']

class PostReactionViewSet(viewsets.ModelViewSet):
    queryset=PostReaction.objects.all()
    serializer_class=PostReactionSerializer
    http_method_names=['get','post','delete']

class PostShareViewSet(viewsets.ModelViewSet):
    queryset=PostShare.objects.all()
    serializer_class=PostShareSerializer
    http_method_names=['get','post']

class PostSaveViewSet(viewsets.ModelViewSet):
    queryset=PostSave.objects.all()
    serializer_class=PostSaveSerializer
    http_method_names=['get','post','delete']

class PostCommentViewSet(viewsets.ModelViewSet):
    queryset=PostComment.objects.all()
    serializer_class=PostCommentSerializer
    http_method_names=['get','post']
    
class PostViewViewSet(viewsets.ModelViewSet):
    queryset=PostView.objects.all()
    serializer_class=PostViewSerializer
    http_method_names=['get','post']

class TotalPostReactionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=(PostReaction.objects.values('post').annotate(total_reactions=Count('id')))
    serializer_class=TotalPostReactionSerializer
    http_method_names=['get']
class TotalPostShareViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=(PostShare.objects.values('post').annotate(total_shares=Count('id')))
    serializer_class=TotalPostShareSerializer
    http_method_names=['get']
class TotalPostSaveViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=(PostSave.objects.values('post').annotate(total_saves=Count('id')))
    serializer_class=TotalPostSaveSerializer
    http_method_names=['get']
class TotalPostCommentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=(PostComment.objects.values('post').annotate(total_comments=Count('id')))
    serializer_class=TotalPostCommentSerializer
    http_method_names=['get']

class TotalPostViewViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = (PostView.objects.values("post").annotate(total_views=Count("id")))
    serializer_class = TotalPostViewSerializer
    http_method_names=['get']
    # def list(self, request):
    #     total_views=PostView.objects.count()
    #     return JsonResponse({'total_video_views':total_views})

    

    
    


    
