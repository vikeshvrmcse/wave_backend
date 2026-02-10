from rest_framework import serializers
from .models import *

class VideoReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=VideoReaction
        fields='__all__'
        
class VideoViewSerializer(serializers.ModelSerializer):
    class Meta:
        model=VideoView
        fields='__all__'
        

class VideoShareSerializer(serializers.ModelSerializer):
    class Meta:
        model=VideoShare
        fields='__all__'

class VideoDownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model=VideoDownload
        fields='__all__'
        
class VideoSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model=VideoSave
        fields='__all__'
        
class VideoCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=VideoComment
        fields='__all__'

class TotalVideoReactionSerializer(serializers.Serializer):
    video=serializers.IntegerField()
    total_reactions=serializers.IntegerField()

class TotalVideoViewSerializer(serializers.Serializer):
    video=serializers.IntegerField()
    total_views=serializers.IntegerField()
    # class Meta:
    #     model=VideoView
    #     fields='__all__'

class TotalVideoShareSerializer(serializers.Serializer):
    video=serializers.IntegerField()
    total_shares=serializers.IntegerField()
class TotalVideoSaveSerializer(serializers.Serializer):
    video=serializers.IntegerField()
    total_saves=serializers.IntegerField()
class TotalVideoCommentSerializer(serializers.Serializer):
    video=serializers.IntegerField()
    total_comments=serializers.IntegerField()
class TotalVideoDownloadSerializer(serializers.Serializer):
    video=serializers.IntegerField()
    total_downloads=serializers.IntegerField()




    
class PostReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostReaction
        fields='__all__'
        
class PostViewSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostView
        fields='__all__'


class PostShareSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostShare
        fields='__all__'

        
class PostSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostSave
        fields='__all__'
        
class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostComment
        fields='__all__'

class TotalPostReactionSerializer(serializers.Serializer):
    post=serializers.IntegerField()
    total_reactions=serializers.IntegerField()
class TotalPostShareSerializer(serializers.Serializer):
    post=serializers.IntegerField()
    total_shares=serializers.IntegerField()
class TotalPostSaveSerializer(serializers.Serializer):
    post=serializers.IntegerField()
    total_saves=serializers.IntegerField()
class TotalPostViewSerializer(serializers.Serializer):
    post=serializers.IntegerField()
    total_views=serializers.IntegerField()
    # class Meta:
    #     model=PostView
    #     fields='__all__'
class TotalPostCommentSerializer(serializers.Serializer):
    post=serializers.IntegerField()
    total_comments=serializers.IntegerField()
    # class Meta:
    #     model=PostView
    #     fields='__all__'