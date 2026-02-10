from django.contrib import admin
from .models import UserModel, VideoModel, PostModel
# Register your models here.
admin.site.register(UserModel)
admin.site.register(VideoModel)
admin.site.register(PostModel)

class UserAdmin(admin.ModelAdmin):
    list_display=('user_name','user_email','user_password', 'user_profile_image')
