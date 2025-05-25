from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    is_admin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "is_admin"
        ]

    def get_is_admin(self, obj):
        return obj.is_staff


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "is_admin",
            "token"
        ]

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
