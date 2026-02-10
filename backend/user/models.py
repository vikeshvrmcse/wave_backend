from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
from datetime import timedelta
from cloudinary.models import CloudinaryField
# Create your models here.
class UserModel(models.Model):
    user_name=models.CharField(max_length=50)
    user_email=models.CharField(max_length=100)
    user_password=models.CharField(max_length=128)
    # user_profile_image=models.FileField(upload_to='user_profile_image/',null=True, blank=True)

    #OTP Fields
    user_profile_image = CloudinaryField('user_profile_image',null=True,blank=True)
    otp=models.CharField(max_length=6, null=True, blank=True)
    otp_expiry_time=models.DateTimeField(null=True, blank=True)
    is_verified=models.BooleanField(default=False)
    
    
    def save(self, *args, **kwargs):
        if not self.user_password.startswith('pbkdf2_'):
            self.user_password=make_password(self.user_password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.user_password)

    def is_otp_valid(self, otp):
        return (self.otp==otp and self.otp_expiry_time and timezone.now()<=self.otp_expiry_time)

    def __str__(self):
        return self.user_name
            
    


class VideoModel(models.Model):
    id = models.BigAutoField(primary_key=True)

    user = models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True,blank=True)
    video_title = models.CharField(max_length=100)
    video_description = models.TextField()
    video_banner = CloudinaryField('user_video_banner',resource_type='image', null=True, blank=True)
    video_file = CloudinaryField('user_video',resource_type='video', null=True, blank=True)
    video_upload_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.video_title



class PostModel(models.Model):
    user=models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)
    post_title=models.CharField(max_length=255)
    post_description=models.TextField()
    post_images=CloudinaryField('user_post_images', resource_type='image', null=True, blank=True)
    post_created_datetime=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title
