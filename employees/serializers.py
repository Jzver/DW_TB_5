from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from employees.models import Employee
from task_tracker.serializers import TaskSerializer


class EmployeeSerializer(ModelSerializer):
    """Сериализатор модели работника.

    Этот сериализатор преобразует экземпляры модели Employee в
    JSON-формат и обратно. Он включает все поля модели.

    Атрибуты:
        Meta (class): Определяет модель и поля, которые будут сериализованы.
    """

    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeTaskSerializer(TaskSerializer):
    """Сериализатор модели работника с подсчетом активных задач.

    Этот сериализатор расширяет TaskSerializer, добавляя информацию о
    задачах работника и количестве активных задач.

    Атрибуты:
        tasks (list): Список задач, связанных с работником.
        active_tasks_count (int): Количество активных задач у работника.
        Meta (class): Определяет модель и поля, которые будут сериализованы.
    """

    tasks = TaskSerializer(many=True, read_only=True)
    active_tasks_count = SerializerMethodField()

    class Meta:
        model = Employee
        fields = (
            "id",
            "full_name",
            "post",
            "tasks",
            "active_tasks_count",
        )

    def get_active_tasks_count(self, obj):
        """Возвращает количество активных задач у работника.

        Аргументы:
            obj (Employee): Экземпляр модели Employee.

        Возвращает:
            int: Количество активных задач.
        """
        return obj.tasks.count()  # Предполагается, что у объекта есть связь с задачами
