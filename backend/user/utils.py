import random
from django.utils import timezone
from datetime import timedelta

from django.core.mail import send_mail
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
def generate_otp():
    return str(random.randint(100000, 999999))

def otp_expiry_time():
    return timezone.now()+timedelta(minutes=5)

def send_otp_email(email, otp):
    send_mail(

subject="Your OTP Verification Code",
message=f"Your OTP is {otp}. It is valid for 5 minutes.",
from_email=settings.EMAIL_HOST_USER,
recipient_list=[email],
fail_silently=False

        )

def get_tokens_for_user(user):
    refresh=RefreshToken.for_user(user)
    return {'refresh':str(refresh), 'access':str(refresh.access_token)}