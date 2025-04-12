Вот исправленная и правильно отформатированная версия вашего README:

markdown
Copy
# BookManagerAPI

API для управления книгами с использованием Django REST Framework.

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/Oblivorten/BookManagerAPI.git
cd BookManagerAPI
Создайте и активируйте виртуальное окружение:

bash
Copy
python3 -m venv venv
# Для Linux/Mac:
source venv/bin/activate
# Для Windows:
venv\Scripts\activate
Установите зависимости:

bash
Copy
pip install -r requirements.txt
Выполните миграции базы данных:

bash
Copy
python manage.py migrate
Запустите сервер:

bash
Copy
python manage.py runserver
API будет доступен по адресу: http://127.0.0.1:8000/api/

Эндпоинты API
Регистрация пользователя
POST /api/register/

Тело запроса:

json
Copy
{
    "username": "your_username",
    "password": "your_password"
}
Получение токена
POST /api/token/

Тело запроса:

json
Copy
{
    "username": "your_username",
    "password": "your_password"
}
Работа с книгами
GET /api/books/ - Получить список книг
POST /api/books/ - Создать новую книгу
PUT /api/books/{id}/ - Обновить книгу
DELETE /api/books/{id}/ - Удалить книгу