from django.db import models
from user.models import UserModel, VideoModel, PostModel
# Create your models here.


class VideoReaction(models.Model):
    LIKE = "like"
    DISLIKE = "dislike"

    REACTION_CHOICES = [
        (LIKE, "Like"),
        (DISLIKE, "Dislike"),
    ]
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE)
    video=models.ForeignKey(VideoModel, on_delete=models.CASCADE)
    
    reaction=models.CharField(max_length=10, choices=REACTION_CHOICES)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=('user', 'video')
    

class VideoView(models.Model):
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE)
    video=models.ForeignKey(VideoModel, on_delete=models.CASCADE)
    watch_time=models.PositiveBigIntegerField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

class VideoShare(models.Model):
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE)
    video=models.ForeignKey(VideoModel, on_delete=models.CASCADE)
    platform = models.CharField(max_length=20,choices=[("link", "Link"), ("whatsapp", "WhatsApp"), ("instagram", "Instagram")])
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ("user", "video", "platform")

class VideoDownload(models.Model):
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE)
    video=models.ForeignKey(VideoModel, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

class VideoSave(models.Model):
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE)
    video=models.ForeignKey(VideoModel, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ("user", "video")

class VideoComment(models.Model):
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE)
    video=models.ForeignKey(VideoModel, on_delete=models.CASCADE)
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
class PostReaction(models.Model):
    LIKE = "like"
    DISLIKE = "dislike"

    REACTION_CHOICES = [
        (LIKE, "Like"),
        (DISLIKE, "Dislike"),
    ]
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE)
    post=models.ForeignKey(PostModel, on_delete=models.CASCADE)
    reaction=models.CharField(max_length=20,choices=REACTION_CHOICES)
    created_at=models.DateTimeField(auto_now_add=True)

    
    class Meta:
        unique_together=('user', 'post')
    


class PostView(models.Model):
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE)
    post=models.ForeignKey(PostModel, on_delete=models.CASCADE)
    watch_time=models.PositiveBigIntegerField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
class PostShare(models.Model):
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE)
    post=models.ForeignKey(PostModel, on_delete=models.CASCADE)
    platform = models.CharField(max_length=20,choices=[("link", "Link"), ("whatsapp", "WhatsApp"), ("instagram", "Instagram")])
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ("user", "post", "platform")

class PostSave(models.Model):
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE)
    post=models.ForeignKey(PostModel, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ("user", "post")
    
class PostComment(models.Model):
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE)
    post=models.ForeignKey(PostModel, on_delete=models.CASCADE)
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)