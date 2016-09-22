
from django.template import RequestContext
from blog.models import Tag,Hit

def global_data(request):

    return {
        'title' : 'Adong的博客',
        'header': 'Adong的博客',
        'tags': Tag.objects.all(),
        'hit':Hit.objects.get(id=1),
    }
