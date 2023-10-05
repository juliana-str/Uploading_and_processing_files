[![Uploading_and_processing_files_workflow](https://github.com/juliana-str/Uploading_and_processing_files/actions/workflows/main.yml/badge.svg)](https://github.com/juliana-str/Uploading_and_processing_files/actions/workflows/main.yml)
# "Загрузка и обработка файлов" (Uploading_and_processing_files)

## 1. [Описание](#1)
## 2. [Установка Docker (на платформе Ubuntu)](#2)
## 3. [База данных и переменные окружения](#3)
## 4. [Команды для запуска](#4)
## 5. [Примеры запросов к api](#5)
## 6. [Техническая информация](#6)
## 7. [Об авторе](#7)

---
## 1. Описание <a id=1></a>

Проект "Загрузка и обработка файлов" (Uploading_and_processing_files) 
позволяет загружать файлы на сервер, а затем асинхронно обрабатывать их с 
использованием Celery.

https://uploadproject.hopto.org/api/

---
## 2. Установка Docker (на платформе Ubuntu) <a id=2></a>

Проект поставляется в контейнерах Docker (db, backend, nginx).  
Для запуска необходимо установить Docker и Docker Compose.  
Подробнее об установке на других платформах можно узнать на [официальном сайте](https://docs.docker.com/engine/install/).

Для начала необходимо скачать и выполнить официальный скрипт:
```bash
apt install curl
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

При необходимости удалить старые версии Docker:
```bash
apt remove docker docker-engine docker.io containerd runc 
```

Установить пакеты для работы через протокол https:
```bash
apt update
```
```bash
apt install \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg-agent \
  software-properties-common -y 
```

Добавить ключ GPG для подтверждения подлинности в процессе установки:
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

Добавить репозиторий Docker в пакеты apt и обновить индекс пакетов:
```bash
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" 
```
```bash
apt update
```

Установить Docker(CE) и Docker Compose:
```bash
apt install docker-ce docker-compose -y
```

Проверить что  Docker работает можно командой:
```bash
systemctl status docker
```

Подробнее об установке можно узнать по [ссылке](https://docs.docker.com/engine/install/ubuntu/).

---
## 3. База данных и переменные окружения <a id=3></a>

Проект использует базу данных PostgreSQL.  
Для подключения и выполненя запросов к базе данных необходимо создать и заполнить файл ".env" с переменными окружения в корне проекта.

Шаблон для заполнения файла ".env":
```python
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
SECRET_KEY='Здесь указать секретный ключ'
ALLOWED_HOSTS='Здесь указать имя или IP хоста' (Для локального запуска - 127.0.0.1)
```

---
## 4. Команды для запуска <a id=4></a>

Перед запуском необходимо склонировать проект:
```bash
git clone https://github.com/juliana-str/Uploading_and_processing_files.git

```

Cоздать и активировать виртуальное окружение:
```bash
python -m venv venv
```
```bash
Linux: source venv/bin/activate
Windows: source venv/Scripts/activate
```

И установить зависимости из файла requirements.txt:
```bash
python3 -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Далее необходимо собрать образы для фронтенда и бэкенда.  
Из папки "./backend/" выполнить команду:
```bash
docker build -t username/uploading_and_processing_files_backend .
```

Из папки "./nginx/" выполнить команду:

```bash
docker build -t username/uploading_and_processing_files_nginx .
```

После создания образов можно создавать и запускать контейнеры. 
Из корня проекта выполнить команду:
```bash
docker-compose up -d
```

После успешного запуска контейнеров выполнить миграции:
```bash
docker-compose exec backend python manage.py migrate
```

Создать суперюзера (Администратора):
```bash
docker-compose exec backend python manage.py createsuperuser
```

Собрать статику:
```bash
docker-compose exec backend python manage.py collectstatic --no-input
```

Теперь доступность проекта можно проверить по адресу [http://localhost/](http://localhost/)

---

## 5. Примеры запросов к api <a id=5></a>

Отправить POST-запрос на добавление нового файла на эндпоинт /api/upload/

Пример запроса: 

```
{
    "file": "http://uploadproject.hopto.org/media/api/media/racion-chernogo-aista.jpg",
    "uploaded_at": "2023-10-04T12:58:37.432541Z",
    "processed": false
}
```

Отправить GET-запрос на просмотр списка загруженных файлов на эндпоинт /api/files/


Пример ответа: 

```
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "file": "http://uploadproject.hopto.org/media/api/media/racion-chernogo-aista.jpg",
            "uploaded_at": "2023-10-04T12:58:37.432541Z",
            "processed": true
        }
    ]
}
```

## 6. Техническая информация <a id=6></a>

Стек технологий: Python 3, Django, Django Rest, Docker, PostgreSQL, nginx, gunicorn, Celery, Redis, github-actions, CI-CD.

Веб-сервер: nginx (контейнер nginx)  
Backend фреймворк: Django (контейнер backend)  
API фреймворк: Django REST (контейнер backend)  
База данных: PostgreSQL (контейнер db)

---
## 7. Об авторе <a id=7></a>

Стрельникова Юлиана Сергеевна  
Python-разработчик (Backend)  
Россия, г. Санкт-Петербург                                                                                                                                                   
E-mail: julianka.str@yandex.ru  
Telegram: @JulianaStr
