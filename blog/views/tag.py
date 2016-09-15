from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from blog.models import Post
from blog.models import Tag

def load(request,id):
    t = Tag.objects.get(id=id)
    p = t.post_set.all().order_by('-updateDatetime')
    return render( request, 'blog/content.html' ,{ 'posts' : p} ) 
