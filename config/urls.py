from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# Представление схемы для документации API
schema_view = get_schema_view(
    openapi.Info(
        title="Документация API",
        default_version="v1",
        description="Описание вашего API",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
    path("employees/", include("employees.urls", namespace="employees")),
    path("task_tracker/", include("task_tracker.urls", namespace="task_tracker")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

"""
Конфигурация URL для проекта Django.

Этот модуль определяет шаблоны URL для приложения, включая:

- Административный интерфейс: доступен по адресу /admin/
- Эндпоинты, связанные с пользователями: доступны по адресу /users/
- Эндпоинты, связанные с сотрудниками: доступны по адресу /employees/
- Эндпоинты трекера задач: доступны по адресу /task_tracker/
- Swagger UI для документации API: доступен по адресу /swagger/
- ReDoc для документации API: доступен по адресу /redoc/

Документация API генерируется с использованием библиотеки drf-yasg и доступна публично.
"""
