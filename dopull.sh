#!/bin/bash
cd $(dirname $0)
git stash
git pull

mv  app/settings.py   app/settings.py.1
cat app/settings.py.1 | sed "s/'USER': 'sa',/'USER': 'blogRoot',/g" > app/settings.py 
mv  app/settings.py   app/settings.py.1
cat app/settings.py.1 | sed "s/'PASSWORD': 'sa',/'PASSWORD': 'blogRoot,123',/g" > app/settings.py
