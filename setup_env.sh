#!/bin/bash

python3 -m venv venv
source venv/bin/activate
pip install pipenv
test -f Pipfile && pipenv install --dev
deactivate
