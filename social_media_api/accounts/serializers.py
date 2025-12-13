from rest_framework import serialzers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework_simplejwt.serialzers import TokenObtainedPairSerializer

class UserRegistrationSerializer(serialzers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class CustomTokenObtainPairSerializer(TokenObtainedPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token
