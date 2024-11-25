from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from task_tracker.models import Task
from task_tracker.serializers import MainTaskSerializer, TaskSerializer


class TaskCreateAPIView(CreateAPIView):
    """Создание задачи.

    Этот класс предоставляет API для создания новой задачи.
    Использует сериализатор TaskSerializer для валидации и
    сохранения данных задачи.

    Атрибуты:
        serializer_class (TaskSerializer): Сериализатор, используемый для создания задачи.
    """

    serializer_class = TaskSerializer


class TaskListAPIView(ListAPIView):
    """Просмотр листа задач.

    Этот класс предоставляет API для получения списка всех задач.
    Использует сериализатор TaskSerializer для преобразования данных
    задач в JSON-формат.

    Атрибуты:
        serializer_class (TaskSerializer): Сериализатор, используемый для отображения задач.
        queryset (QuerySet): Набор данных задач, который будет возвращен.
    """

    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskRetrieveAPIView(RetrieveAPIView):
    """Просмотр задачи.

    Этот класс предоставляет API для получения конкретной задачи по её идентификатору.
    Использует сериализатор TaskSerializer для преобразования данных задачи в JSON-формат.

    Атрибуты:
        serializer_class (TaskSerializer): Сериализатор, используемый для отображения задачи.
        queryset (QuerySet): Набор данных задач, который будет использован для поиска.
    """

    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskUpdateAPIView(UpdateAPIView):
    """Редактирование задачи.

    Этот класс предоставляет API для обновления существующей задачи.
    Использует сериализатор TaskSerializer для валидации и сохранения
    обновленных данных задачи.

    Атрибуты:
        serializer_class (TaskSerializer): Сериализатор, используемый для редактирования задачи.
        queryset (QuerySet): Набор данных задач, который будет использован для поиска.
    """

    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskDestroyAPIView(DestroyAPIView):
    """Удаление задачи.

    Этот класс предоставляет API для удаления существующей задачи.
    Использует queryset для определения задачи, которую необходимо удалить.

    Атрибуты:
        queryset (QuerySet): Набор данных задач, который будет использован для поиска.
    """

    queryset = Task.objects.all()


class TaskImportantListAPIView(ListAPIView):
    """Поиск менее загруженных сотрудников.

    Этот класс предоставляет API для получения списка задач, которые
    имеют активные подзадачи и не имеют назначенного исполнителя.
    Использует сериализатор MainTaskSerializer для преобразования данных
    задач в JSON-формат.

    Атрибуты:
        serializer_class (MainTaskSerializer): Сериализатор, используемый для отображения задач.
        queryset (QuerySet): Набор данных задач, который будет возвращен.

    Методы:
        get_queryset(): Переопределяет метод для фильтрации задач по определенным критериям.
    """

    serializer_class = MainTaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        """Фильтрует задачи для получения только тех, которые имеют активные подзадачи
        и не имеют назначенного исполнителя.

        Возвращает:
            QuerySet: Набор отфильтрованных задач.
        """
        return Task.objects.filter(
            other__employee__isnull=False,
            other__status="start",
            employee__isnull=True,
            status="start",
        )
