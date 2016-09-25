from django.core.mail import send_mail
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django import forms

import hashlib
import datetime

from blog.views.userForm import UserForm
from blog.models import User

def inner_gethash(text) :
    hash = hashlib.sha1()
    hash.update(text.encode('utf-8'))
    return hash.hexdigest()

def inner_setcookie(response, value) :
    tm = datetime.datetime.now()
    tm = tm + datetime.timedelta(days = 365)
    response.set_cookie('cookie_userid', value, expires = tm)

def userReg(request):

    errors = None
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                tu = User.objects.filter(nickname_email = cd['nickname_email'])
                if tu.count() > 0 :
                    errors = '登录名已存在！'
                tu = User.objects.filter(name = cd['name'])
                if tu.count() > 0 :
                    errors = '姓名已存在!'
                if len(cd['password']) < 6 and len(cd['password1']) < 6 :
                    errors = '密码至少要6个字符!'
                if cd['password'] != cd['password1'] :
                    errors = '密码和密码确认不同！'
                if errors == None :
                    u = User()
                    u.name = cd['name']
                    u.nickname_email = cd['nickname_email']
                    u.password = inner_gethash(cd['password'])
                    u.ismember = cd['ismember']
                    u.save()
                    
                    response =  HttpResponseRedirect('/blog/user/regThanks/')

                    if u.ismember :
                        inner_setcookie(response, u.id)
                        
                    return response
            except :
                errors =  "用户注册错误！"
    else:
        form = UserForm()

    return render(request, 'blog/userReg.html',{'form' : form, 'errors' : errors })

def thanks(request):
    return render(request, 'blog/userRegThanks.html',{})
