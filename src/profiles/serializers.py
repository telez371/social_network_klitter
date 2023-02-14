from rest_framework import serializers
from .models import UserNet

class GetUserNetSerializer(serializers.ModelSerializer):
    """Вывод информации о пользователе"""
    avatar = serializers.ImageField(write_only=True)
    class Meta:
        model = UserNet
        exclude = (
            "last_login", "password", "is_active",
            "is_staff", "is_superuser", "groups",
            "user_permissions",
        )

class GetUserPublicSerializer(serializers.ModelSerializer):
    """Вывод публичной информации о пользователе"""
    class Meta:
        model = UserNet
        exclude = (
            "phone", "email", "last_login", "password",
            "is_active", "is_staff", "is_superuser",
            "groups", "user_permissions",
        )



class UserByFollowerSerializer(serializers.ModelSerializer):
        """Сериалайзер для подписчиков"""
        avatar = serializers.ImageField(write_only=True)
        class Meta:
            model = UserNet
            fields = ('id', 'username', 'avatar')
