#!/bin/bash
cd $(dirname $0)
git stash
git pull

cat app/settings.py | sed "s/'USER': 'sa',/'USER': 'blogRoot',/g" > app/settings.py 
cat app/settings.py | sed "s/'PASSWORD': 'sa',/'PASSWORD': 'blogRoot,123',/g" > app/settings.py
