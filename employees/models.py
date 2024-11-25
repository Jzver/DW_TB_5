from django.db import models

NULLABLE = {"blank": True, "null": True}


class Employee(models.Model):
    """Модель работника.

    Эта модель представляет сотрудника в системе и содержит информацию
    о его полном имени и должности.

    Атрибуты:
        full_name (CharField): Полное имя сотрудника, максимальная длина - 100 символов.
        post (CharField): Должность сотрудника, максимальная длина - 100 символов.
    """

    full_name = models.CharField(
        max_length=100, verbose_name="Full Name", help_text="Введите ФИО"
    )
    post = models.CharField(
        max_length=100, verbose_name="Post", help_text="Введите должность", **NULLABLE
    )

    def __str__(self):
        """Возвращает полное имя сотрудника как строковое представление."""
        return self.full_name

    class Meta:
        """Метаданные для модели Employee."""

        verbose_name = "Employee"
        verbose_name_plural = "Employees"
