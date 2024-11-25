from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from users.models import User
from users.serializers import MyTokenObtainPairSerializer, UserSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    """Создание JWT-токена для аутентификации пользователя.

    Этот класс использует сериализатор MyTokenObtainPairSerializer для
    генерации токена, который будет использоваться для аутентификации
    пользователей в приложении.
    """

    serializer_class = MyTokenObtainPairSerializer


class UserCreateAPIView(CreateAPIView):
    """Создание нового пользователя.

    Этот класс предоставляет API для создания нового пользователя.
    Использует сериализатор UserSerializer для валидации и сохранения
    данных пользователя.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        """Сохраняет новый пользовательский объект.

        Args:
            serializer (User Serializer): Сериализатор, используемый для
            создания нового пользователя.

        Этот метод устанавливает пароль для пользователя в зашифрованном
        виде и сохраняет его в базе данных.
        """
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
