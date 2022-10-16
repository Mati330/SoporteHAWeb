#!/usr/bin/env bash
# exit on error
set -o errexit

# poetry install <- este no, estoy usando requirements.txt ( que ya la pagina de render nos lo da)

python manage.py collectstatic --no-input
python manage.py migrate