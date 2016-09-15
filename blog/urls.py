from django.conf.urls import url
from blog.views import index as blog_index
from blog.views import post as blog_post
from blog.views import tag as blog_tag

urlpatterns = [
    url(r'^$' , blog_index.load ),
    url(r'^post/(\d+)$', blog_post.load),
    url(r'^tag/(\d+)$', blog_tag.load),
]
