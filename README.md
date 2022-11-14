# maps_with_django

## Creating web app with Python, Django and PostgreSQL database

sudo apt-get install gdal-bin
sudo apt-get install libpq5


# if you are on Linux you need to install also

    sudo apt install postgis postgresql-13-postgis-3

    postgres=# create database mydb;
    CREATE DATABASE
    postgres=# create user myuser with encrypted password 'mypass';
    CREATE ROLE
    postgres=# grant all privileges on database mydb to myuser;
    GRANT
    ALTER USER myuser WITH SUPERUSER;
    \du
    connect myuser: psql --host=localhost --port=5432 --username=myuser --password --dbname=mydb
    * CREATE EXTENSION postgis;
    * CREATE EXTENSION postgis_topology;

python3 manage.py migrate