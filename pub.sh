#!/bin/bash

cd $(dirname $0)

if [ ! $# == 3 ]; then
    echo "用法: $0 服务器数据库用户名 密码 发送邮件邮箱密码"
    exit
fi

mysqlusername=$1
mysqluserpassword=$2
sendemailpassword=$3

git add .
git commit -m "$(date +%Y%m%d)"
git push

ssh t.rstone.com.cn ~/website/dopull.sh $mysqlusername $mysqluserpassword $sendemailpassword

