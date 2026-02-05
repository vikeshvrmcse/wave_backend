from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RegisterAPIView,
    LoginAPIView,
    VerifyOTPAPIView,
    ResendOTPAPIView,
    VideoViewSet,
    # ProfileImageUploadAPIView,
    GetAllUserAPIViewSet
)

router = DefaultRouter()
router.register(r'users', GetAllUserAPIViewSet, basename='users')
router.register(r'videos', VideoViewSet, basename='videos')
urlpatterns = [
    # AUTH APIs
    path('register/', RegisterAPIView.as_view()),
    path('verify-otp/', VerifyOTPAPIView.as_view()),
    path('resend-otp/', ResendOTPAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    # path('upload-profile-image/', ProfileImageUploadAPIView.as_view()),

    # LIST USERS API
    path('', include(router.urls)),
]
