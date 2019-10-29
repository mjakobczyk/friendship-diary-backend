#!/bin/bash

# Language
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

# Flask
export FLASK_APP=startup.py
export FLASK_DEBUG=1

# Config
export APP_CONFIG_FILE=config.py

# Testing
export TESTING=False

# Secret
export SECRET_KEY=123

# PostgreSQL
export POSTGRES_URL=127.0.0.1:5432
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=password
export POSTGRES_DB=postgres

# Database
export SQLALCHEMY_DATABASE_URI=
export SQLALCHEMY_TRACK_MODIFICATIONS=False

flask run --host=0.0.0.0