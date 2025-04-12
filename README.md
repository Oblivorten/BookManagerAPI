BookManagerAPI
API для управления книгами с использованием Django REST Framework (DRF) и токен-авторизацией. Пользователи могут регистрироваться, а также добавлять, редактировать, удалять и просматривать свои книги.

🚀 Технологии
Django — фреймворк для веб-разработки на Python.

Django REST Framework (DRF) — для создания RESTful API.

Token Authentication — аутентификация через токен.

Django Filters — для фильтрации и поиска.

Django Pagination — для пагинации.

📦 Установка
Клонируйте репозиторий:

bash
Копировать
Редактировать
git clone https://github.com/Oblivorten/BookManagerAPI.git
cd BookManagerAPI
Создайте и активируйте виртуальное окружение:

bash
Копировать
Редактировать
python3 -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate     # для Windows
Установите зависимости:

bash
Копировать
Редактировать
pip install -r requirements.txt
Выполните миграции базы данных:

bash
Копировать
Редактировать
python manage.py migrate
Запустите сервер:

bash
Копировать
Редактировать
python manage.py runserver
API будет доступен по адресу http://127.0.0.1:8000/api/.

📑 Эндпоинты API
POST /api/register/ — Регистрация нового пользователя.

Тело запроса:

json
Копировать
Редактировать
{
  "username": "your_username",
  "password": "your_password"
}
POST /api/token/ — Получить токен для аутентификации.

Тело запроса:

json
Копировать
Редактировать
{
  "username": "your_username",
  "password": "your_password"
}
GET /api/books/ — Получить список книг пользователя (пагинированный).

Заголовок: Authorization: Token <your_token>

Параметры поиска: ?genre=...&author=...&name=...

POST /api/books/ — Создать новую книгу.

Тело запроса:

json
Копировать
Редактировать
{
  "name": "Название книги",
  "author": "Автор книги",
  "age": 200,
  "genre": "Жанр книги"
}
PUT /api/books/{id}/ — Обновить книгу.

DELETE /api/books/{id}/ — Удалить книгу.

🔑 Аутентификация
Для взаимодействия с защищёнными эндпоинтами (например, создание/редактирование книг) необходимо передавать токен авторизации в заголовке запроса:

bash
Копировать
Редактировать
Authorization: Token <your_token>
Токен можно получить, отправив запрос на /api/token/ с вашими логином и паролем.

💡 Особенности
Аутентификация через токены.

Пагинация, поиск и фильтрация по книгам.

Книги принадлежат пользователю, и каждый пользователь может управлять только своими книгами.

Регистрация и аутентификация пользователей через API.