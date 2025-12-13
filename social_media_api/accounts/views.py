from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .serializers import UserRegistrationSerializer, UserSerialzer, LoginSerializer
# from django.conf import settings

# Create your views here.
User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serialzer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serialzer = self.get_serializer(data=request.data)
        serialzer.is_valid(raise_exception=True)
        user = serialzer.save()

        # token_serializer = CustomTokenObtainPairSerializer()
        # tokens = token_serializer.get_token(user)

        return Response({
            "message": "User registered successfully"
        }, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    permission_classes = [AllowAny]
    serialzer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "token": token.key,
            "user": UserSerialzer(user).data,
        }, status.HTTP_200_OK)


class ProfileManagementView(generics.RetrieveUpdateAPIView):
    serialzer_class = UserSerialzer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class FollowUserView(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        target_user = self.grt_object()
        current_user = request.user

        if current_user == target_user:
            return Response({"detail": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)

        current_user.following.add(target_user)
        return Response({
            "detail": f"You are now following {target_user.username}."
        },status=status.HTTP_200_OK)

class UnfollowUserView(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        target_user = self.get_object()
        current_user = request.user

    if current_user == target_user:
        return Response({"detail": "You cannot unfollow yourself."}, status.HTTP_400_BAD_REQUEST)

    current_user.following.remove(target_user)
    return Response({"detail": f"You have unfollowed {target_user.username}."}, 
    status=status.HTTP_200_OK)


# CustomUser.objects.all()