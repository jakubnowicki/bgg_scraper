#!/bin/bash

python3 -m venv venv
source venv/bin/activate
pip install pipenv
[ -f Pipfile ] && { echo "Pipfile exists, installing dependencies"; pipenv install --dev ;}
deactivate
echo "Setup finished"
