#!/bin/bash
git add .
git commit -m "$(date +%Y%m%d)"
git push

ssh t.rstone.com.cn ~/website/dopull.sh

