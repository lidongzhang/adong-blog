from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from blog.models import Post

def load(request):
    p = Post.objects.all().order_by('-updateDatetime')
    return render( request, 'blog/postList.html' ,{ 'posts' : p} )
