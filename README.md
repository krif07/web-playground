<<<<<<< HEAD
# Hyperblog 💚
Un blog increíble para el[ curso de Git y Github](https://platzi.com/cursos/git-github/ " curso de Git y Github") de [Platzi](https://platzi.com/ "Platzi")
> El curso de Git y Github de Platzi es lo que me hacía falta para triplicar mi salario y lanzarme a la industria del tejido de lana sintética con Machine Learning
> - niñita

## En este curso vemos de todo
* Todos los comandos de Git
* El flujo de trabajo en Github
* El verdadero amor por las buenas prácticas
* Trucos muy locos del profesor
* Las personalidades múltiples de Freddy
* Colaborador Krif
* Incluye ejemplos multiplataforma
* Disponible todas las edades

Y como un amable recordatorio: **Este readme.md es un chiste**.  Diseñado para el ejemplo. Si llegas acá NO TE LO TOMES EN SERIO y mejor ve [**a ver el curso**](https://platzi.com/cursos/git-github/ "a ver el curso").
=======
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
>>>>>>> 12351da (Fixin git error)
