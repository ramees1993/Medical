#!/usr/bin/env bash

set -o errexit  # Exit script on any error

pip install -r requirements.txt  # Correct pip command

python manage.py collectstatic --no-input  # Collect static files

python manage.py migrate  # Apply database migrations
