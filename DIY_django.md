# DIY Django Project

# Environment setup

1. Cookiecutter
2. Virtualenvwrapper
3. PostgresDB
4. Django


# Cookiecutter
Django’s startproject command allows you to create and use simple Django project
templates. However, over time the controls (deployment, front end tooling, etc) around a
project grow more and more complex. Most of us hit the limitations of startproject
quickly and need a more powerful project templating tool. Hence the use of Cookiecutter
(cookiecutter.readthedocs.io), an advanced project templating tool that can be used
for generating Django project boilerplate.

Installation instruction: [Cookiecutter-Github](https://github.com/cookiecutter/cookiecutter-django)

Install it with
```
pip install cookiecutter"
```

Run int against the repo:
```
cookiecutter https://github.com/cookiecutter/cookiecutter-django
```
Choose project specifications.

# Virtualenvwrapper

Follow the [instructions](https://virtualenvwrapper.readthedocs.io/).

Add following lines to your shell startup file
```
source <path-to-your-virtualenvwrapper.sh>
```
Follow the instructions:
```
pip install virtualenvwrapper
export WORKON_HOME=~/Envs
mkdir -p $WORKON_HOME
$ source <path-to-your-virtualenvwrapper.sh>
$ mkvirtualenv <your-environment-name>
```
If you get an error during the `source`-command, try to add following line to your shell startup file:
```
export VIRTUALENVWRAPPER_PYTHON=/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
```
Create a virtual environment for your project:
```
mkvirtualenv <your-environment-name>
```
Activate it
```
workon <your-environment-name>
```
Install the dependencies by navigating to the root folder of the project you just created with cookiecutter
and running
```
pip install -r requirements/local.txt
```


## Troubleshooting

### pg_config executable not found
On Mac OS X, this issue was solved by installing postgresql using the homebrew package manager
```
brew install postgresql
```

### Can't find location of virtualenvwrapper
If you cannot find the installation folder try to
```
pip uninstall virtualenvwrapper
```
Then the folder will be shown. Cancel the uninstall process.


# PostgresDB

See [cookiecutter docs](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html).

Install Postgres from [official site](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)

Create a new PostgreSQL database using createdb:
```
createdb --username=postgres <project_slug>
```
Set the environment variables for your database(s):
```
export DATABASE_URL=postgres://postgres:<password>@127.0.0.1:5432/<DB name given to createdb>
```

# Django

Apply migrations:
```
python manage.py migrate
```
See the application being served through Django development server:
```shell
python manage.py runserver 0.0.0.0:8000
```







