#!/bin/zsh
python3 -m venv env
source env/bin/activate env
pip install -r requirements.txt
django-admin startproject admin
cd admin
python3 manage.py runserver
