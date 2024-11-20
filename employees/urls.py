from django.urls import path

from employees.apps import EmployeesConfig
from employees.views import (EmployeeCreateAPIView, EmployeeDestroyAPIView,
                             EmployeeListAPIView, EmployeeRetrieveAPIView,
                             EmployeeTaskListAPIView, EmployeeUpdateAPIView)

app_name = EmployeesConfig.name

urlpatterns = [
    path("create/", EmployeeCreateAPIView.as_view(), name="employee-create"),
    path("list/", EmployeeListAPIView.as_view(), name="employee-list"),
    path("<int:pk>/", EmployeeRetrieveAPIView.as_view(), name="employee-retrieve"),
    path("update/<int:pk>/", EmployeeUpdateAPIView.as_view(), name="employee-update"),
    path("delete/<int:pk>/", EmployeeDestroyAPIView.as_view(), name="employee-delete"),
    path("employee_task/", EmployeeTaskListAPIView.as_view(), name="employee-task"),
]