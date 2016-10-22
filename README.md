# eventloggr

Collect (via HTTP API) loglines of services (simple script), 
store them (in a database) 
&amp; notify other services (for example chat bots).


## Install

1. clone the repo
2. run `pip install -r requirements.txt`

## Run

run `python manage.py runserver`


## Deploy

Use [Gunicorn](http://gunicorn.org/) (or [uWSGI](http://projects.unbit.it/uwsgi)) and [nginx](https://nginx.org/). See [Deploying Django](https://docs.djangoproject.com/en/1.10/howto/deployment/).

Don't forget to change the config in `eventloggr/settings.py` (database stuff and `SECRET_KEY`!).
