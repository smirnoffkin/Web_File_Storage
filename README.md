This is a simple REST API project with FastAPI, PostgreSQL and SQLAlchemy.  
View the detailed task in [TASK.md](./enrollment/Task.md).  
  
Running  
------------
### With Docker ###
Just:
~~~
docker-compose up --build
~~~
But be sure that nothing else is running on 80(api) and 5432(db) ports.  
It will build docker image and then start it and another container with PostgreSQL.  
After that you will be able to access api on 0.0.0.0 or 127.0.0.1 or localhost.

### Without Docker ###
If you don't have **docker** then you need:
1. Install **[PostgreSQL](https://www.postgresql.org)**
2. Configure it to listen on *localhost*
3. Make some superuser with some password
4. Go to ./app folder in **[database.py](./app/database.py)** file and change the DATABASE_URL for your database:
~~~
DATABASE_URL = "postgresql://<your_user>:<your_password>@<your_db_hostname>/<your_db_name>"
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

Features
------------
FastAPI also provides automated API documentation.  
To do this, just go to the 127.0.0.1:<your_port>/docs or 127.0.0.1:<your_port>/redoc, where you can test all CRUD methods.

###### P.S. ######
In the submitted task (the enrollment folder), some variables are named inconsistently with PEP8 (such as "parentId").  
In order not to rewrite unit_test and not get confused in the names among the models, I decided to use the same names.