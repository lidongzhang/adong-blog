from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from blog.models import Post

def load(request,id):
    p = Post.objects.get(id=id)
    return render( request, 'blog/post.html' ,{ 'post' : p} ) 
