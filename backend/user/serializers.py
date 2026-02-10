from rest_framework import serializers
from .models import UserModel, VideoModel, PostModel

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserModel
        fields=['user_name', 'user_email', 'user_password','user_profile_image']
        extra_kwargs={'user_password':{'write_only':True}}

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserModel
        exclude=("otp", "otp_expiry_time", "user_password","is_verified")

# class ProfileImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserModel
#         fields = ["user_profile_image"]
        
class OTPVerifySerializer(serializers.Serializer):
    email=serializers.EmailField()
    otp=serializers.CharField(max_length=6)

class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()


class ResendOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()


from rest_framework import serializers
from .models import VideoModel



class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoModel
        fields = [
            'id',
            'video_title',
            'video_description',
            'video_banner',
            'video_file',
        ]

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostModel
        fields = '__all__'
    


