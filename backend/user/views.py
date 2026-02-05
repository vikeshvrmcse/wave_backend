from django.shortcuts import render
from django.http import JsonResponse
from .models import UserModel, VideoModel
from .utils import generate_otp, send_otp_email, otp_expiry_time, get_tokens_for_user
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import (RegisterSerializer, OTPVerifySerializer, LoginSerializer, ResendOTPSerializer, UserSerializer, VideoSerializer)

class RegisterAPIView(APIView):
    queryset=UserModel.objects.all()
    serializer_class=RegisterSerializer
    def post(self, request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            otp=generate_otp()
            user=serializer.save(otp=otp, otp_expiry_time=otp_expiry_time())
            send_otp_email(user.user_email, otp)
            return Response({"message":"OTP to sent email"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

class VerifyOTPAPIView(APIView):
    def post(self, request):
        serializer=OTPVerifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email=serializer.validated_data['email']
        otp=serializer.validated_data['otp']

        try:
            user=UserModel.objects.get(user_email=email)
        except UserModel.DoesNotExist:
            return Response({'error':"User not found"}, status=404)

        if user.otp==otp and user.otp_expiry_time>=timezone.now():
            user.is_verified=True
            user.otp=None
            user.otp_expiry_time=None
            user.save()
            return Response({"message":"OTP verified successfully"})
        return Response({"error":"Invalid or expired OTP"}, status=400)

class LoginAPIView(APIView):
    queryset=UserModel.objects.all()
    serializer_class=LoginSerializer
    def post(self, request):
        serializer=LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email=serializer.validated_data['email']
        password=serializer.validated_data['password']
        try:
            user=UserModel.objects.get(user_email=email)
        except UserModel.DoesNotExist:
            return Response({'error':"Invalid credentials"}, status=400)
        if not user.is_verified:
            return Response({"error":"OTP not verified"}, status=403)
        if user.check_password(password):
            tokens=get_tokens_for_user(user)
            return Response({"message":"Login successful", "tokens":str(tokens)})

        return Response({"error":"Invalid credential"}, status=400)


class ResendOTPAPIView(APIView):
    def post(self, request):
        serializer = ResendOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        try:
            user = UserModel.objects.get(user_email=email)
        except UserModel.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
        if user.is_verified:
            return Response({"message": "User already verified"})
        otp = generate_otp()
        user.otp = otp
        user.otp_expiry_time = otp_expiry_time()
        user.save()
        send_otp_email(email, otp)
        return Response({"message": "OTP resent successfully"})

    

class GetAllUserAPIViewSet(viewsets.ModelViewSet):
    queryset=UserModel.objects.all()
    serializer_class=UserSerializer
    



class VideoViewSet(viewsets.ViewSet):
    # queryset = VideoModel.objects.all()
    # serializer_class = VideoSerializer
    # parser_classes = [MultiPartParser, FormParser]
    def list(self, request):
        videos=VideoModel.objects.all()
        serializer=VideoSerializer(videos, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        id=pk
        if id is not None:
            video=VideoModel.objects.get(id=id)
            serializer=VideoSerializer(video)
            return Response(serializer.data)
        return Response({"message":"Id is missing"}, status=status.HTTP_400_BAD_REQUEST)
    

    def create(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')

        if not user_id:
            return Response(
                {"error": "user_id is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = UserModel.objects.get(id=user_id)
        except UserModel.DoesNotExist:
            return Response(
                {"error": "Invalid user"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(
                {"message": "Video uploaded successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        user_id=pk
        video=VideoModel.objects.get(pk=user_id)
        serializer=VideoSerializer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Video Updated successfully"},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        user_id=pk
        video=VideoModel.objects.get(pk=user_id)
        serializer=VideoSerializer(video, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Updated successfull"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk):
        user_id=pk
        video=VideoModel.objects.get(pk=user_id)
        if video:
            video.delete()
            return Response({"message":"Video Deletion successfull"}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)