from django.contrib import admin
from task_tracker.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Админ-интерфейс для модели Task.

    Этот класс управляет отображением и поведением модели Task в админ-панели Django.
    Он настраивает, какие поля будут отображаться в списке задач, а также может
    включать дополнительные настройки для фильтрации, поиска и редактирования задач.

    Атрибуты:
        list_display (tuple): Параметр, определяющий, какие поля модели
                              будут отображаться в списке задач в админке.
    """

    list_display = ("id", "name", "deadline", "status")
