# Bulletin Board

Приветствуем вас в проекте "Bulletin Board" - это простой веб-сервис для создания объявлений.

## Описание проекта

Этот проект представляет собой доску объявлений, где пользователи могут размещать свои объявления и оставлять отзывы.

## Особенности

- **Объявления:** Создавайте объявления с указанием заголовка, цены, описания и других деталей.
- **Отзывы:** Пользователи могут оставлять отзывы к объявлениям.
- **Пользователи:** Регистрируйтесь, входите в систему и управляйте своим профилем и объявлениями.
- **Роли:** Реализованные роли для управления веб сервисом админ и пользователь.
  
## Технологии

- Фреймворк Django Rest Framework
- Djoser
- База данных PostgreSQL
- Язык программирования Python
- Git
- Docker
- Docker-compose

## Установка и запуск 

Следуйте этим шагам для установки и запуска проекта.

### Клонирование проекта

git clone https://github.com/burnaschev/Bulletin_board.git


### Создание и активация виртуального окружения

python3 -m venv venv
source venv/bin/activate

### Переменные окружения

Все необходимые переменные окружения находятся в файле .env_sample

Нужно создать свой переменные окружения в файле .env

### Установка зависимостей

pip install -r requirements.txt


### Запуск сервера 

python manage.py runserver

После чего вы сможете получить доступ к API по адресу `http://localhost:8000/`.


## Docker

Если вы предпочитаете использовать Docker:

1. Соберите образ:

    ```bash
    docker-compose build
    ```

2. Запустите контейнер:

    ```bash
    docker-compose up -d
    ```

Приложение будет доступно по адресу http://localhost:8080/.

## API Documentation

API documentation can be found at `http://localhost:8000/docs/`.
