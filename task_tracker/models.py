from django.db import models
from employees.models import Employee

NULLABLE = {"blank": True, "null": True}

TASK_STATUS = [
    ("start", "start"),
    ("finish", "finish"),
]

FATHER_TASK = [("father", "father"), ("other", "other")]


class Task(models.Model):
    """Модель задачи.

    Эта модель представляет собой задачу в системе. Она связывает задачи с исполнителями и
    позволяет организовать иерархию задач через родительские задачи. Каждая задача имеет
    статус, срок исполнения и может быть связана с другим заданием.

    Атрибуты:
        name (str): Наименование задачи. Максимальная длина - 100 символов.
        parent_task (ForeignKey): Ссылка на родительскую задачу (если есть).
                                  Позволяет создавать иерархии задач.
        employee (ForeignKey): Исполнитель задачи, связанный с моделью Employee.
        deadline (DateField): Срок исполнения задачи.
        status (str): Статус задачи, может быть 'start' или 'finish'.
    """

    name = models.CharField(
        max_length=100, verbose_name="Name", help_text="Введите наименование задачи"
    )
    parent_task = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="other",
        help_text="Введите родительскую задачу",
        **NULLABLE
    )
    employee = models.ForeignKey(
        Employee,
        verbose_name="Executor",
        related_name="tasks",
        on_delete=models.CASCADE,
        help_text="Введите исполнителя",
        **NULLABLE
    )
    deadline = models.DateField(
        verbose_name="Deadline", help_text="Введите срок исполнения", **NULLABLE
    )
    status = models.CharField(
        choices=TASK_STATUS,
        default=TASK_STATUS[0][0],
        verbose_name="Status",
        help_text="Введите статус",
    )

    def __str__(self):
        """Возвращает строковое представление задачи.

        Возвращает наименование задачи, которое будет использоваться
        для отображения задачи в интерфейсах.
        """
        return self.name

    class Meta:
        """Метаданные модели Task."""

        verbose_name = "Task"
        verbose_name_plural = "Tasks"
