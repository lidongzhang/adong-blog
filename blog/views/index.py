from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from blog.models import Post,Hit

def load(request):
    p = Post.objects.all().order_by('-updateDatetime')
    hit = Hit.objects.get(id=1)
    hit.count = hit.count + 1
    hit.save()
    return render( request, 'blog/content.html' ,{ 'posts' : p} ) #此处必须要这么写否则 context_processors中的函数不会运行
