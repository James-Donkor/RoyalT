#!/bin/bash
source .venv/bin/activate
export $(grep -v '^#' .env | xargs)
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
