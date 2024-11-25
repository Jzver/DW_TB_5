from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    """Модель пользователя, наследующаяся от AbstractUser.

    Этот класс определяет поля и поведение модели User в приложении.
    """

    username = None
    """Удаляем поле username, чтобы использовать email как уникальный идентификатор."""

    email = models.EmailField(
        unique=True,
        verbose_name="Email Address",
        max_length=255,
        help_text="Введите почту",
    )
    """Поле email, используемое как уникальный идентификатор пользователя."""

    phone = models.CharField(
        max_length=35,
        verbose_name="Phone Number",
        help_text="Введите телефон",
        **NULLABLE
    )
    """Поле phone, хранящее номер телефона пользователя."""

    USERNAME_FIELD = "email"
    """Определяем поле email как уникальный идентификатор пользователя."""

    REQUIRED_FIELDS = []
    """Список обязательных полей для создания пользователя."""

    # Переопределяем поля groups и user_permissions
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',
        blank=True,
    )
    """Поле groups, хранящее группы, к которым принадлежит пользователь."""

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',
        blank=True,
    )
    """Поле user_permissions, хранящее права доступа пользователя."""

    def __str__(self):
        """Метод для строкового представления объекта User."""
        return self.email

    class Meta:
        """Мета-информация модели User."""
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
