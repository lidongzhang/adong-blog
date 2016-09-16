#!/bin/bash
cd $(dirname $0)

mysqlusername=$1
mysqluserpassword=$2
sendemailpassword=$3

git add .
git stash
git pull

mv  app/settings.py   app/settings.py.1
cat app/settings.py.1 | sed "s/'USER': 'sa',/'USER': '$(mysqlusername)',/g" > app/settings.py 

mv  app/settings.py   app/settings.py.1
cat app/settings.py.1 | sed "s/'PASSWORD': 'sa',/'PASSWORD': '$(mysqluserpassword)',/g" > app/settings.py

mv  app/settings.py   app/settings.py.1
cat app/settings.py.1 | sed "s/EMAIL_HOST_PASSWORD = ''/EMAIL_HOST_PASSWORD = '$(sendemailpassword)'/g"

rm app/settings.py.1

python3 manage.py makemigrations
python3 manage.py migrate
