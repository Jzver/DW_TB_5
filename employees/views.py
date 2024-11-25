from django.db.models import Count, Q
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from employees.models import Employee
from employees.serializers import EmployeeSerializer, EmployeeTaskSerializer


class EmployeeCreateAPIView(CreateAPIView):
    """Создание нового работника.

    Это представление обрабатывает запросы на создание нового работника
    в системе. Использует сериализатор EmployeeSerializer для валидации
    и сохранения данных.

    Атрибуты:
        serializer_class (EmployeeSerializer): Сериализатор для создания работника.
    """

    serializer_class = EmployeeSerializer


class EmployeeListAPIView(ListAPIView):
    """Просмотр списка работников.

    Это представление возвращает список всех работников в системе.
    Использует сериализатор EmployeeSerializer для преобразования данных
    в формат JSON.

    Атрибуты:
        serializer_class (EmployeeSerializer): Сериализатор для отображения работников.
        queryset (QuerySet): Запрос для получения всех работников.
    """

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeRetrieveAPIView(RetrieveAPIView):
    """Просмотр информации о работнике.

    Это представление возвращает детальную информацию о конкретном работнике
    по его идентификатору. Использует сериализатор EmployeeSerializer для
    преобразования данных в формат JSON.

    Атрибуты:
        serializer_class (EmployeeSerializer): Сериализатор для отображения работника.
        queryset (QuerySet): Запрос для получения всех работников.
    """

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeUpdateAPIView(UpdateAPIView):
    """Редактирование информации о работнике.

    Это представление обрабатывает запросы на обновление информации о работнике
    в системе. Использует сериализатор EmployeeSerializer для валидации и
    сохранения измененных данных.

    Атрибуты:
        serializer_class (EmployeeSerializer): Сериализатор для редактирования работника.
        queryset (QuerySet): Запрос для получения всех работников.
    """

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeDestroyAPIView(DestroyAPIView):
    """Удаление работника.

    Это представление обрабатывает запросы на удаление работника из системы
    по его идентификатору.

    Атрибуты:
        queryset (QuerySet): Запрос для получения всех работников.
    """

    queryset = Employee.objects.all()


class EmployeeTaskListAPIView(ListAPIView):
    """Просмотр списка работников с подсчетом активных задач.

    Это представление возвращает список работников, у которых есть активные задачи.
    Использует сериализатор EmployeeTaskSerializer для отображения работников
    с количеством активных задач.

    Атрибуты:
        queryset (QuerySet): Запрос для получения всех работников.
        serializer_class (EmployeeTaskSerializer): Сериализатор для отображения работников с задачами.

    Методы:
        get_queryset(): Переопределяет метод для получения работников с подсчетом активных задач.
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeTaskSerializer

    def get_queryset(self):
        """Возвращает список работников с подсчетом активных задач.

        Этот метод аннотирует queryset работников, добавляя количество активных задач
        и фильтруя работников, у которых есть хотя бы одна активная задача.

        Возвращает:
            QuerySet: Работники с активными задачами, отсортированные по количеству активных задач.
        """
        return (
            Employee.objects.annotate(
                active_tasks_count=Count("tasks", filter=Q(tasks__status="start"))
            )
            .filter(active_tasks_count__gt=0)
            .order_by("-active_tasks_count")
        )
