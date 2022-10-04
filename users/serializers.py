from rest_framework import serializers

from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    birthdate = serializers.DateField()
    bio = serializers.CharField(allow_blank=True, allow_null=True, default=None)
    is_critic = serializers.BooleanField(allow_null=True, default=False)
    updated_at = serializers.DateTimeField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True, default=False)

    def validate_email(self, value: str):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("email already exists")

        return value

    def validate_username(self, value: str):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("username already exists")

        return value

    def create(self, validated_data):

        user = User.objects.create_user(**validated_data)

        return user


class UserCriticSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name"]


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
