from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from employees.models import Employee
from task_tracker.models import Task


class EmployeeTestCase(APITestCase):
    """Тесты для модели работника."""

    def setUp(self):
        """Предварительная настройка для тестов.

        Создает тестового работника, который будет использоваться в тестах.
        """
        self.employee = Employee.objects.create(
            full_name="Тест имя", post="Тест должность"
        )

    def test_employee_create(self):
        """Тест на создание нового работника.

        Проверяет, что новый работник успешно создается через API,
        и что возвращаемые данные соответствуют ожидаемым.
        """
        url = reverse("employees:employee-create")
        data = {"full_name": "Гладков Сергей", "post": "developer"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["full_name"], "Гладков Сергей")
        self.assertEqual(response.data["post"], "developer")
        self.assertEqual(Employee.objects.count(), 2)

    def test_employee_retrieve(self):
        """Тест на получение информации о работнике.

        Проверяет, что информация о существующем работнике
        корректно возвращается через API.
        """
        url = reverse("employees:employee-retrieve", args=(self.employee.id,))
        response = self.client.get(url, format="json")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["full_name"], self.employee.full_name)
        self.assertEqual(data["post"], self.employee.post)

    def test_employee_update(self):
        """Тест на обновление информации о работнике.

        Проверяет, что информация о работнике корректно обновляется
        через API и возвращаемые данные соответствуют ожидаемым.
        """
        url = reverse("employees:employee-update", args=(self.employee.id,))
        response = self.client.patch(
            url, data={"full_name": "updated name", "post": "update developer"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["full_name"], "updated name")
        self.assertEqual(response.data["post"], "update developer")

    def test_employee_delete(self):
        """Тест на удаление работника.

        Проверяет, что работник успешно удаляется через API
        и что количество работников в базе данных уменьшается.
        """
        url = reverse("employees:employee-delete", args=(self.employee.id,))
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), 0)

    def test_employee_list(self):
        """Тест на получение списка работников.

        Проверяет, что список работников корректно возвращается
        через API и что количество работников соответствует ожидаемому.
        """
        url = reverse("employees:employee-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Employee.objects.count(), 1)

    def test_employee_task_list(self):
        """Тест для подсчета активных задач работника.

        Проверяет, что количество активных задач для работника
        корректно возвращается через API.
        """
        Task.objects.create(
            name="Test task",
            employee=self.employee,
            deadline=None,
            status="start",
            parent_task=None,
        )
        url = reverse("employees:employee-task")
        response = self.client.get(url, format="json")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data[0]["active_tasks_count"], 1)
