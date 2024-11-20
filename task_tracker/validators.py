import re
from rest_framework.serializers import ValidationError


class NameValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        # Обновленное регулярное выражение для проверки всей строки, а не только начала
        reg = re.compile("^[а-яА-Яa-zA-Z0-9.,\\-\\ ]+$")  # Добавлено + для проверки всей строки
        tmp_val = dict(value).get(self.field)

        # Проверка на пустое значение
        if tmp_val is None or not tmp_val.strip():
            raise ValidationError("Поле не может быть пустым.")

        # Валидация входного значения по регулярному выражению
        if not reg.match(tmp_val):
            raise ValidationError(
                "Поле принимает только буквы, цифры, запятую, точку, тире и пробел."
            )
