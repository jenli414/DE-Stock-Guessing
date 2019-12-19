#!/bin/bash
source $(python3 -m pipenv --venv)/bin/activate
export PYTHONPATH=.
export FLASK_APP=./app.py
python3 app.py
