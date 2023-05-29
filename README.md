# DanasQuest

## Django Setup

### Steps:

1. Cookiecutter
2. Virtualenvwrapper
3. PostgresDB
4. Django
5. Git
6. Tailwind
7. Start Development of a new App

## Cookiecutter 
Django’s startproject command allows you to create and use simple Django project
templates. However, over time the controls (deployment, front end tooling, etc) around a
project grow more and more complex. Most of us hit the limitations of startproject
quickly and need a more powerful project templating tool. Hence the use of Cookiecutter
(cookiecutter.readthedocs.io), an advanced project templating tool that can be used
for generating Django project boilerplate.

Installation instruction: [Cookiecutter-Github](https://github.com/cookiecutter/cookiecutter-django)

Install Cookiecutter with
```
pip install cookiecutter
```
Navigate to your root folder for the project.
Run cookiecutter against its django-repo to create the folder structure and other 
boilerplate files:
```
cookiecutter https://github.com/cookiecutter/cookiecutter-django
```
If you have already downloaded it, choose delete and re-download.

Choose project specifications.

## Virtualenvwrapper

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
source <path-to-your-virtualenvwrapper.sh>
```

If you get an error during the `source`-command, try to add following line to your shell startup file:
```
export VIRTUALENVWRAPPER_PYTHON=/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
```
Create a virtual environment for your project, e.g. in `~/.virtualenvs/` 
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
pip3 install -r requirements/local.txt
```


## Troubleshooting

### Pycharm error: Django is not importable in this environment
Clear caches by going `File` > `Invalidate Caches` / `Restart`...

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


## PostgresDB

See [cookiecutter docs](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html).

Install Postgres from [official site](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)

Create a new PostgreSQL database using createdb:
```
createdb --username=postgres <project_slug>
```

If you get an error `psql: error: connection to server on socket "/tmp/.s.PGSQL.5432" failed: ...`
that means that postgresql didn't start properly. Try to navigate to your postgres folder
it is either in `/usr/local/var/postgres/` or `/opt/homebrew/var/postgresql@14/` and then:
1. stop the service `brew services stop postgresql` 
2. remove `postmaster.pid` if it exists
3. in file `postgresql.conf` either uncomment or change the line `port = 5432`
4. restart your machine

Set the environment variables for your database(s):
```
export DATABASE_URL=postgres://postgres:<password>@127.0.0.1:5432/<DB name given to createdb>
```

You can use `pgadmin` to manage the postgres servers and work with your databases.  

## Django
### Create migrations
```
python manage.py makemigrations
```
### Apply migrations
```
python manage.py migrate
```
This should create the default tables in your database.

If you get an error like `ModuleNotFoundError: No module named 'environ'`
run `pip3 install environ` to install the missing module.

### Apply fixtures
In order to load initial data in to the enum-tables run following 
script for **every** fixture.  
```
python manage.py loaddata <path-to-fixture-file>
```
e.g:
```
python manage.py loaddata daya_commons.json
python manage.py loaddata daya_categories.json
```
### Start application
See the application being served through Django development server:
```shell
python manage.py runserver 0.0.0.0:8000
```

## Git

1. Create a git repo.
2. Navigate to the root folder of the project and init a git repo:
```
git init
```
3. Add remote repo to your local git
```shell
git remote add origin <path-your-repo.git>
```
4. Create the initial branch. Normally called `main` or `master`
```
git branch -M <branch-name>
```
5. Create your first commit using either the IDE or
```
git commit -m "your-commmit-message"
```
6. Push your commit either through the IDE or 
```
git push -u origin <branch-name>
```
Your first commit is pushed!


## Tailwind
Follow the official [tutorial](https://tailwindcss.com/docs/installation).

Install Tailwind CSS 
```
npm install -D tailwindcss
```

Create config file for tailwind:
```
npx tailwindcss init
```
This creates a file `tailwind.config.js`.
Adding anything to this file is optional. 
If you leave any parts blank, Tailwind will use its default 
configuration options, which you can view [here](https://github.com/tailwindlabs/tailwindcss/blob/master/stubs/defaultConfig.stub.js). 
The Tailwind docs recommend filling in only the options you want changed, rather than including the full default config file (which you can do by using npx tailwindcss init --full when initiating the project).

Add path to your templates, e.g: 
```
  ...
  content: [
      "./daya/templates/**/*.{html,js}",
  ],
  ...
```
Add following lines to `./daya/static/css/project.css`
```
@tailwind base;
@tailwind components;
@tailwind utilities;
```
Build css classes with:
```
npx tailwindcss -i ./daya/static/css/project.css -o ./daya/static/css/tailwind.css --watch
```
This will build the tailwind's css automatically whenever a file in the templates folder is updated.

Add 
```
<link href="{% static 'css/tailwind.css' %}" rel="stylesheet">
```
to your header.

## Development
  
### Shell
Activate shell:
```
python manage.py shell
```

### Create superuser:
```
python manage.py createsuperuser --username=joe --email=joe@example.com
```
Enter a password.

### App Development
In order to start a new app (another module in your project) run following commands:
1. Create the `<name-of-the-app>` app with 
```
python manage.py startapp <name-of-the-app>
``` 
2. Move `<name-of-the-app` directory to `<project_slug>` directory
3. Edit `<project_slug>/<name-of-the-app>/apps.py` and change 
```
name = "<name-of-the-app>"
```
to 
```
name = "<project_slug>.<name-of-the-app>"
```
4. Add `"<project_slug>.<name-of-the-app>.apps.<NameOfTheAppConfigClass>"` to `LOCAL_APPS` in `config/settings/base.py`


### Add new packages to virtual environment

If you add new packages to virtual environment don't forget to add them to requirements files by:
``` shell
python -m pip freeze > requirements/tmp.txt
python -m pip freeze > requirements/base.txt
python -m pip freeze > requirements/local.txt
python -m pip freeze > requirements/production.txt
```

### Localization
In order to translate messages insert 
```
from django.utils.translation import gettext_lazy as _
```
inside `config/settings/base.py`. And after the line:
```
LANGUAGE_CODE = "en-us"
```
put:
```
LANGUAGES = [
   ('de', _('German')),
   ('en', _('English')),
]
```
or whatever language you need. Then create `locale/de` and `locale/en` folders.

Now you can run
```
python manage.py makemessages --all
```
to create the messages and translations. Open `locale/de/LC_MESSAGES/django.po`
and translate your all your messages.
Now run 
```
python manage.py compilemessages
```
to compile the messages.
