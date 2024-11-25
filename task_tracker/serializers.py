from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueTogetherValidator

from employees.models import Employee
from task_tracker.models import Task
from task_tracker.validators import NameValidator


class TaskSerializer(ModelSerializer):
    """Сериализатор модели задачи.

    Этот сериализатор преобразует экземпляры модели Task в JSON-формат
    и обратно. Он включает в себя валидацию уникальности имени задачи и
    дополнительные проверки через NameValidator.

    Атрибуты:
        Meta (class): Внутренний класс, определяющий модель, поля и валидаторы.
    """

    class Meta:
        model = Task
        fields = "__all__"
        validators = [
            NameValidator(field="name"),
            UniqueTogetherValidator(fields=["name"], queryset=Task.objects.all()),
        ]


class MainTaskSerializer(ModelSerializer):
    """Сериализатор для поиска менее загруженных сотрудников.

    Этот сериализатор используется для получения списка задач и
    определения доступных сотрудников, которые имеют наименьшую
    загрузку по текущим задачам.

    Атрибуты:
        tasks (TaskSerializer): Сериализованные задачи, связанные с родительской задачей.
        available_employees (SerializerMethodField): Список сотрудников с наименьшей загрузкой.

    Методы:
        get_available_employees(task): Определяет сотрудников с наименьшим количеством активных задач.
    """

    tasks = TaskSerializer(source="other", many=True)
    available_employees = SerializerMethodField()

    class Meta:
        model = Task
        fields = "__all__"

    def get_available_employees(self, task):
        """Определяет сотрудников с наименьшим количеством активных задач.

        Этот метод проверяет всех сотрудников, подсчитывает количество
        активных задач у каждого и возвращает список имен сотрудников,
        имеющих наименьшую загрузку. Также добавляет сотрудников, которые
        являются исполнителями дочерних задач текущей задачи.

        Аргументы:
            task (Task): Экземпляр текущей задачи, для которой ищутся доступные сотрудники.

        Возвращает:
            list: Список имен сотрудников с наименьшей загрузкой.
        """
        employees = Employee.objects.all()
        emp_data = {}
        for emp in employees:
            list_task = emp.tasks.filter(status="start")
            emp_data[emp.pk] = len(list_task)
        min_count = min(emp_data.values())
        available_employees = [
            emp.full_name for emp in employees if emp_data[emp.pk] == min_count
        ]
        for emp in employees:
            tasks = Task.objects.filter(parent_task=task.id)
            for t in tasks:
                if t.employee == emp and emp.full_name not in available_employees:
                    available_employees.append(emp.full_name)
        return available_employees
