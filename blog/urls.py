from django.conf.urls import url
from blog.views import index as blog_index

urlpatterns = [
    url(r'^$' , blog_index.load ),
]
