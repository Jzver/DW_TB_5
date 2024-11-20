# MVP - Трекер задач сотрудников.  

Cерверное приложение для работы с базой данных, представляющее собой трекер задач сотрудников. В приложение есть CRUD операции для сотрудников и задач, а также два специальных эндпоинта для получения информации о загруженности сотрудников и важных задачах.

Трекер задач позволит компании эффективно управлять заданиями, назначенными сотрудникам. Это поможет в равномерном распределении нагрузки между сотрудниками и своевременном выполнении ключевых задач.

## Для запуска проекта локально потребуется:
1. Установите Git и Docker
2. Клонировать репозиторий. https://github.com/Jzver/DW_TB_5
3. Создайте и заполнить файл .env своими данными.
4. Запустите терминал и выполните команды: docker-compose build  , docker-compose up
5. Если требуется доступ к админке, выполните команду: docker-compose exec app python manage.py csu (Создает супер пользователя email="admin@gmail.com"  password="22092013")

### CRUD URL
- [POST] http://localhost:8000/employees/create/ - Создание юзера.
- [POST] http://localhost:8000/users/token/ - Создание JWT токена.

- [GET] http://localhost:8000/employees/list/ - Просмотр листа работников.
- [GET] http://localhost:8000/employees/{id}/ - Просмотр работника.
- [POST] http://localhost:8000/employees/create/ - Создание работника.
- [PATCH] http://localhost:8000/employees/update/{id}/ - Редактирование работника.
- [DELETE] http://localhost:8000/employees/delete/{id}/ - Удаление работника.
- 
- [GET] http://localhost:8000/task_tracker/list/ - Просмотр листа задач.
- [GET] http://localhost:8000/task_tracker/{id}/ - Просмотр задачи.
- [POST] http://localhost:8000/task_tracker/create/ - Создание задачи.
- [PATCH] http://localhost:8000/task_tracker/update/{id}/ - Редактирование задачи.
- [DELETE] http://localhost:8000/task_tracker/delete/{id}/ - Удаление задачи.

- http://127.0.0.1:8000/swagger/, http://127.0.0.1:8000/redoc/ - документация для API

### Специализированные URL
- [GET] http://localhost:8000/employees/employee_task/ - Просмотр для подсчета активных задач работника.
- [GET] http://localhost:8000/task_tracker/tracker/ - Поиск менее загруженных сотрудников.


полная документация http://localhost:8000/redoc/ или http://localhost:8000/swagger/