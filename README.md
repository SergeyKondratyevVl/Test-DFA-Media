# Test-DFA-Media

Запуск:
```
docker-compose up --build
```

Реализовано:
- Всё сделать в виде АПИ (в DRF)
- CRUD к картинкам
- Сделать роут для удаления всех картинок из базы для администратора
- Любая авторизация, регистрация
- Роут на получение текущего юзера
- Покрытие кода тестами
- Контейнеризация

Вам обязательно понадобится файл .env в папке config со следующими параметрами:
- DEBUG
- SECRET_KEY
- POSTGRES_ENGINE=django.db.backends.postgresql_psycopg2
- POSTGRES_DB
- POSTGRES_USER
- POSTGRES_PASSWORD
- POSTGRES_HOST=postgres
- POSTGRES_PORT=5432
- REDIS_HOST=redis
- REDIS_PORT=6379

Для тестирования используется SQLite3.
