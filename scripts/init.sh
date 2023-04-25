#!/bin/bash
echo hello world
echo "Hello $USER"
echo "Today is $(date)"
echo "Bye for now"

echo "======================================================================="
echo "Install minimal packages"
echo "======================================================================="

sudo apt-get update

echo "======================================================================="
echo "Install application"
echo "======================================================================="

sudo apt-get install python3-pip python3-dev
sudo apt install virtualenv

git clone repository.url.git

cd $repository
virtualenv venv -p python3


sudo apt-get install libpq-dev postgresql postgresql-contrib
sudo -u postgres psql
# execute sql init file

# Execute Update application script

python ./manage.py createsuperuser


echo "======================================================================="
echo "Install HTTP server"
echo "======================================================================="

sudo apt-get install nginx

# Create configuration file and link
sudo touch /etc/nginx/sites-available/webapp_name
sudo ln -s /etc/nginx/sites-available/webapp_name /etc/nginx/sites-enabled

# Set webapp_name config file

# Remove default link (or remove redundant domain name in this default file)
sudo rm /etc/nginx/site-enabled/default
# Reload NGinx service
sudo service nginx reload

echo "======================================================================="
echo "Install Webapp server Gunicorn"
echo "======================================================================="

sudo apt-get install supervisor
sudo vi /etc/supervisor/conf.d/webapp-gunicorn.conf

# set webapp-gunicorn.conf

# Run supervisor processus
sudo supervisorctl reread
sudo supervisorctl update

echo "======================================================================="
echo "Update application"
echo "======================================================================="

# Execute Update application script

