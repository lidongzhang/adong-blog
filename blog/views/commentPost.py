from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
import hashlib
import  datetime 

from blog.models import Post, User, Comment
from blog.views.postCommentForm import PostCommentForm

def inner_gethash(text):
    hash = hashlib.sha1()
    hash.update(text.encode('utf-8'))
    return hash.hexdigest()

def inner_postcomment(tu, content, ismember):
    '''postcomment 业务处理'''
    r = {'error' : None, 'name' : None, "cookie" : {'name': None, 'value':None} }
    
    u = None
    u = tu
    if tu.inner_state == "nologin":
        if tu.nickname_email == 'anonymous@rstone.tech' :
            u = User.objects.get(nickname_email = tu.nickname_email)
            u.inner_state = "login"
        else:
            us = User.objects.filter(nickname_email = tu.nickname_email, password = inner_gethash(tu.password))
            if us.count() == 0 :
                r["error"] = "用户名或密码错误！"
            else:
                r["name"] = us[0].name
                u = us[0]
                u.inner_state = "login"

    if u.inner_state == "login"  :
        t = Comment()
        t.userID = u
        t.content = content
        t.save()
        
        if  tu.nickname_email != 'anonymous@rstone.tech' :
            r["name"] = u.name
            r["cookie"]["name"] = "cookie_userid"
            r["cookie"]["value"] = u.id
            r["cookie"]["time"] = None
            if ismember :
                tm = datetime.datetime.now()
                tm = tm + datetime.timedelta(days = 365)
                r["cookie"]["time"] =  tm
    return r

def inner_cookie(u, request) :
    '''cookie处理'''
    cookie_userid = None
    if "cookie_userid" in  request.COOKIES:
        cookie_userid = request.COOKIES["cookie_userid"]

    if cookie_userid :
        tus = User.objects.filter(id = cookie_userid)
        if tus.count() > 0 :
            u = tus[0]
            u.inner_state = "login"
    return u

def inner_print(info, value):
    print(info + ":" , value)

def load(request):

    name = None
    u = User()
    u.inner_state ="nologin"   #'''nologin login'''
    u = inner_cookie(u, request)
    if u.inner_state == "login" :
        name = u.name
    inner_print("inner_state", u.inner_state)
    error = None
    r = None
    if request.method == 'POST':
        form = PostCommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            if u.inner_state == "nologin" :
                u.nickname_email = cd['userNickname_email']
                
                u.password = cd['userPassword']
                u.passowrd = u.password.strip()
                if u.nickname_email == "" :
                    error = '必须输入用户名！'
                
                if u.nickname_email != 'anonymous@rstone.tech':
                    if u.password == "":
                        error = "必须输入密码！"
                    elif len(u.password) < 6 :
                        error = "必须输入6位以上密码！"
            '''业务处理'''
            r = inner_postcomment(u, cd['content'], cd['ismember'])
            
            if r["error"] :
                error = r["error"]
            else:
                cd['content'] = ''
                form = PostCommentForm(cd)
            name = r["name"]

    else:
        #anonymous
        data = {'userNickname_email' : 'anonymous@rstone.tech'  ,
                'ismember' : True   }
        form = PostCommentForm(data)

    #提取本post的 留言
    pc = Comment.objects.filter().order_by('-createDatetime')
    
    response = render( request, 'blog/commentPost.html' ,{ 'form' : form, 'error' : error, 'name' : name, 'pc' : pc} )



    if r :
        inner_print("r", r)
        if  r["cookie"]["name"] :
            response.set_cookie(r["cookie"]["name"], r["cookie"]["value"])
            if r["cookie"]["time"] :
                response.set_cookie(r["cookie"]["name"],r["cookie"]["value"],expires=r["cookie"]["time"])
    #response.delete_cookie('cookie_userid')
    return response

