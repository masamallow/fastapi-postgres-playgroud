FastAPI with PostgreSQL Playground
===

Develop an application using FastAPI and PostgreSQL, following the web article.

## Reference

- Following
    - [FastAPI を使ってWEBアプリを作ってみる　その1 \| nMoMo's](https://nmomos.com/tips/2021/01/23/fastapi-docker-1/)
- Official
    - [FastAPI](https://fastapi.tiangolo.com/ja/)
    - [tiangolo/fastapi: FastAPI framework, high performance, easy to learn, fast to code, ready for production](https://github.com/tiangolo/fastapi)

## Environment & Tool

- Python 3.10
- FastAPI
    - Web Framework
- Mako
    - [welcome to Mako\!](https://www.makotemplates.org/)
    - Template library
- Alembic
    - [Welcome to Alembic’s documentation\! — Alembic 1\.7\.6 documentation](https://alembic.sqlalchemy.org/en/latest/)
    - Migration tool

## Docker Build

```shell
pipenv lock -r > backend/requirements.txt

docker compose up -d --build

# attach server
docker compose exec server /bin/sh

# connect DB
docker compose exec db psql -h localhost -U postgres --dbname=postgres
```

## Migration

ref. [Welcome to Alembic’s documentation\! — Alembic 1\.7\.6 documentation](https://alembic.sqlalchemy.org/en/latest/)

```shell
docker compose exec server /bin/sh

### internal container
# create ddl script from template
alembic revision -m "create_first_tables"
# [!] executed as root

# upgrade
alembic upgrade head
```
