#!/bin/bash
echo hello world
echo "Hello $USER"
echo "Today is $(date)"
echo "Bye for now"


# export ENV=PRODUCTION

cd repository

source venv/bin/activate
python3 -m pip install pip --upgrade
pip install -Ir requirements/base.txt

git pull origin develop

# Update staticfiles
python ./manage.py collectstatic

# Update database
python ./manage.py migrate
python ./manage.py loaddata ./store/dumps/store.json

# Check processus 
sudo supervisorctl status
sudo supervisorctl restart webapp-gunicorn
