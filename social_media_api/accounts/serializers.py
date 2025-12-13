from rest_framework import serialzers
from django.contrib.auth.password_validation import validated_password
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = ('username', 'email')

class UserRegistrationSerializer(serialzers.ModelSerializer):
    password2 = serialzers.CharField(style={'input_type': 'password'}, write_only=True)
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'token']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def get_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj)
        return token.key

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serialzers.ValidationError({"password": "Password fields didn't match."})
        validated_password(data['password'])
        return data


    get_user_model = User
    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
            raise serializers.ValidationError("Invalid credentials")