from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Админ-интерфейс для управления пользователями.

    Этот класс настраивает отображение и функциональность
    модели User в админ-панели Django.

    Атрибуты:
        list_display (tuple): Кортеж полей, которые будут отображаться в списке пользователей.
    """

    list_display = ("id", "email", "phone")
