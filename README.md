# Playgroud
Django project 

# Creating the virtual environment
```sh
python3 -m venv env
cd web-enterprise
source env/bin/activate
# Windows
.\env\Scripts\activate
```

# Creating Project
```sh
pip install django
pip install django-ckeditor
pip install Pillow
pip install pylint
pip install pylint-django
pip install pylint-celery

pip freeze > requirements.txt
```

```sh
# activate virtual environment 
source env/bin/activate

# Create project with name app
django-admin startproject webplayground
cd webplayground/
# Create or modify DB
python3 manage.py makemigrations
python3 manage.py migrate
# Run the project
python3 manage.py runserver

```

# Creating an application within the project
```sh
# activate virtual environment 
source env/bin/activate

cd webplayground/
# create core application
python3 manage.py startapp core

```

# Make migrations of the models
```sh
# activate virtual environment 
source env/bin/activate

cd webplayground/
python3 manage.py makemigrations core
python3 manage.py migrate

```

# Creating a super user
```sh
# activate virtual environment 
source env/bin/activate

python3 manage.py createsuperuser

```
