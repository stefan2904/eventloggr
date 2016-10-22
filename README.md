# eventloggr

Collect loglines of services,  store them &amp; notify other services. 

Build with [Django](https://www.djangoproject.com/), [requests](http://docs.python-requests.org), and [itsdangerous](https://pythonhosted.org/itsdangerous/).

* Collect:
 * Provides simple HTTP endpoint (one or multiple per service)
 * Endpoints secured by [JWT](https://jwt.io)
 * Demo sender script in `scripts/send_data.py`
 * For example: sensor status, build status, change in wiki, ...

* Store:
 * In a database (see [relevant Django docs](https://docs.djangoproject.com/en/1.10/ref/databases/))
 * Inspect & manipulate data via web using [Django admin](https://docs.djangoproject.com/en/1.10/ref/contrib/admin/)
 * Nothing fancy
 
* Notify
 * Define one (or multiple) notifier per service
 * Send out (signed) HTTP request with received data to defined url
 * Again secured by [JWT](https://jwt.io)
 * Trigger action somewhere else that way (webhook, test, build, alarm, chat bot, mail, ...)
   * for example: [eventloggr-telegram](https://github.com/stefan2904/eventloggr-telegram)


## Install

1. clone the repo
2. run `pip install -r requirements.txt`


## Run

run `python manage.py runserver`


## Deploy

Use [Gunicorn](http://gunicorn.org/) (or [uWSGI](http://projects.unbit.it/uwsgi)) and [nginx](https://nginx.org/). See [Deploying Django](https://docs.djangoproject.com/en/1.10/howto/deployment/).

Don't forget to change the config in `eventloggr/settings.py` (database stuff and `SECRET_KEY`!).
