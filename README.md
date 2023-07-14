## Инструкции для запуска проекта:

## Запуск проекта с помощью docker compose
В корневой папке создайте файл с именем  ```.env``` и заполните его по образцу ниже или скопируйте из файла ```example.env``` образец заполнения.

## Пример .env файла:

```
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=your_db_name

SECRET_KEY='django-insecure-05ydg$v@r+5i9gtdjdu5i^%f8apmgq=ec2@7ytb+p1hfji1%tv'

```

|    command    | description   |
|:--------------|:--------------|
| ```git clone https://github.com/AndrewDorniak/SFT.git``` |  Копируем проект        |
| ```cd sft```         | Заходим в папку с проектом        |
| ```cp example.env .env``` |  Создаем .env и заполняем своими крэдами (см. ниже)   |
| ```docker compose -f 'docker-compose.yaml' up --build```       | Запускаем сборку докер контейнера   |
