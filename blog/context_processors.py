
from django.template import RequestContext
from blog.models import Tag

def global_data(request):

    return {
        'title' : 'Adong的博客',
        'header': 'Adong的博客',
        'tags': Tag.objects.all(),
    }