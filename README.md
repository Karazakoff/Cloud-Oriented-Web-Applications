# to run server local
* create virtual env
```bash
python3 -m venv venv
. venv/bin/activate
```
* install requirements
```bash
pip install -r req.txt
```
* create `.env` file for your project (env-example)

* create database in postgresql

* migrate tables to postgresql
```bash
./manage.py migrate
# or
python3 manage.py migrate
```
* run the server
```bash
./manage.py runserver
# or
python3 manage.py runserver
```
* to create superuser (for admin)
```bash
./manage.py createsuperuser
# or
python3 manage.py createsuperuser
```

# run docker container
* change `.env`
* add `DB_HOST=db`
* change `DB_USER=postgres`
* change `DB_PASSWORD=postgres`
* change `DB_NAME=postgres`

```bash
docker-compose build
docker-compose run --service-ports --rm app
```

> Your server will be running on `http://127.0.0.1:8000`
> if you want to look up documentation `http://127.0.0.1:8000/docs`