from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Сериализатор для выдачи JWT-токена.

    Этот сериализатор наследует функциональность TokenObtainPairSerializer
    и добавляет дополнительное поле email в возвращаемый токен.
    """

    @classmethod
    def get_token(cls, user):
        """Генерирует токен для указанного пользователя.

        Args:
            user (User ): Пользователь, для которого создается токен.

        Returns:
            Token: JWT-токен с добавленным полем email.
        """
        token = super().get_token(user)

        token["email"] = user.email

        return token


class UserSerializer(ModelSerializer):
    """Сериализатор для модели пользователя.

    Этот сериализатор преобразует данные модели User в формат,
    который может быть использован для передачи через API.
    """

    class Meta:
        model = User
        fields = ("id", "email", "phone")
        """Список полей, которые будут включены в сериализованный вывод."""
