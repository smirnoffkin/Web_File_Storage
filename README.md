#### English version #####
------------
### This is a simple REST API project with FastAPI, PostgreSQL and SQLAlchemy. ###
### View the detail task in [TASK.md](./enrollment/Task.md). ###
  
Running  
------------
### With Docker ###
Just:
~~~
docker-compose up --build
~~~

### Without Docker ###
If you don't have **docker** then you need:
1. Install **[PostgreSQL](https://www.postgresql.org)**
2. Set up the basic parameters of the Database (superuser, password, port, host, etc.)
3. Create an .env file in the root of the project  
Example .env file:
~~~
POSTGRES_DEALECT_DRIVER=postgresql
POSTGRES_USER=postgres
POSTGRES_PASSWORD=1234
POSTGRES_HOST=localhost
POSTGRES_DB=item_db
POSTGRES_PORT=5432
~~~

Dependencies
------------
Then you need to install the required python packages, just:
~~~
pip install -r requirements.txt
~~~

Then you must first create the database we need:
~~~
python create_db.py
~~~

And finally to run:
~~~
python main.py
~~~

Running Tests
------------
Just:
~~~
pytest -v ./tests/
~~~
Features
------------
FastAPI also provides automated API documentation.  
To do this, just go to the 127.0.0.1:<your_port>/docs or 127.0.0.1:<your_port>/redoc, where you can test all CRUD methods.

###### P.S. ######
In the submitted task (the enrollment folder), some variables are named inconsistently with PEP8 (such as "parentId").  
In order not to rewrite unit_test and not get confused in the names among the models, I decided to use exactly the same names.

  

##### Русская версия #####
------------
### Это простой REST API проект, написанный с использованием FastAPI, PostgreSQL и SQLAlchemy. ###
### Детальное описание задания смотрите в [TASK.md](./enrollment/Task.md). ###
  
Запуск  
------------
### В докере ###
Просто:
~~~
docker-compose up --build
~~~

### Вне докера ###
Если у вас нет докера, вам нужно:
1. Установить **[PostgreSQL](https://www.postgresql.org)**
2. Настроить основные параметры Базы Данных (админ, пароль, порт, хост и тд)
3. Создать в корне проекта .env файл  
Пример .env файла:
~~~
POSTGRES_DEALECT_DRIVER=postgresql
POSTGRES_USER=postgres
POSTGRES_PASSWORD=1234
POSTGRES_HOST=localhost
POSTGRES_DB=item_db
POSTGRES_PORT=5432
~~~

Зависимости
------------
Затем нужно установить необходимые пакеты python, для этого:
~~~
pip install -r requirements.txt
~~~

Затем нужно создать необходимую базу данных:
~~~
python create_db.py
~~~

И наконец запуск приложения:
~~~
python main.py
~~~

Запуск тестов
------------
Просто:
~~~
pytest -v ./tests/
~~~

"Фича"
------------
FastAPI предоставляет автоматическую API документацию.
Для этого пройто перейдите по адресу 127.0.0.1:<ваш_порт>/docs или 127.0.0.1:<ваш_порт>/redoc, где вы можете попробовать все CRUD методы.

###### P.S. ######
В представленном задании (папка enrollment), название некоторых переменных не соответствуют PEP8 (например, "parentId"). Чтобы не переписывать предоставленный unit_test и не запутаться в названиях среди моделей, я решил использовать везде точно такие же названия.