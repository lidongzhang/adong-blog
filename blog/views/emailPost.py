from blog.views.emailForm import EmailForm
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response
from blog.models import Post
from django.http import HttpResponseRedirect
from django import forms

def postEmail(request):

    errors = None
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                send_mail('[adong blog]'  + cd['title'], cd['message'],cd['fromEmail'],['lidongzhang@rstone.com.cn'])
                return HttpResponseRedirect('/blog/emailPost/thanks/')
            except :
                errors =  "邮件发送错误！"
    else:
        form = EmailForm()

    return render(request, 'blog/emailPost.html',{'form' : form, 'errors' : errors })

def thanks(request):
    return render(request, 'blog/emailPostThanks.html',{})
