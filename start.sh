#!/bin/sh

export FLASK_APP=startup.py
export FLASK_DEBUG=1
export APP_CONFIG_FILE=config.py
flask run