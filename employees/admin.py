from django.contrib import admin
from employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """
    Административный интерфейс для модели Employee.

    Этот класс настраивает отображение модели Employee в административной панели Django.

    Атрибуты:
        list_display (tuple): Поля, которые будут отображаться в списке сотрудников.
            - id: Уникальный идентификатор сотрудника.
            - full_name: Полное имя сотрудника.
            - post: Должность сотрудника.
    """

    list_display = ("id", "full_name", "post")
