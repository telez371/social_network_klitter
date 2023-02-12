from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from src.profiles.models import UserNet
from src.profiles.serializers import GetUserNetSerializer, GetUserPublicSerializer


class UserPublicView(ModelViewSet):
    """Вывод публичного профиля пользователя"""
    queryset = UserNet.objects.all()
    serializer_class = GetUserPublicSerializer
    permission_classes = [permissions.AllowAny]



class UserNetView(ModelViewSet):
    """Вывод профиля пользователя"""
    serializer_class = GetUserNetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserNet.objects.filter(id=self.request.user.id)