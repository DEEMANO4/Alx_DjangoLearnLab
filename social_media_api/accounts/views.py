from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from .serialzers import UserRegistrationSerializer, CustomTokenObtainPairSerializer

# Create your views here.

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serialzer_class = UserRegistrationSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serialzer = self.get_serializer(data=request.data)
        serialzer.is_valid(raise_exception=True)
        user = serialzer.save()

        token_serializer = CustomTokenObtainPairSerializer()
        tokens = token_serializer.get_token(user)

        return Response({
            "user": serialzer.data,
            "refresh": str(tokens)
            "access": str(tokens.access_token),
        }, status=status.HTTP_201_CREATED)

class CustomTokenObtainPairView(TokenObtainView):
    serializer_class = CustomTokenObtainPairSerializer
