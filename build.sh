#!/usr/bin/env bash
# exit on error
set -o errexit

# poetry install <- este no, estoy usando requirements.txt 
pip freeze > requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate