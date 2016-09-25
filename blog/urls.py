from django.conf.urls import url
from blog.views import index as blog_index
from blog.views import post as blog_post
from blog.views import tag as blog_tag
from blog.views import postList as blog_postList
from blog.views import emailPost as blog_emailPost
from blog.views import userReg as blog_userReg
from blog.views import commentPost as blog_commentPost

urlpatterns = [
    url(r'^$' , blog_index.load ),
    url(r'^post/(\d+)$', blog_post.load),
    url(r'^tag/(\d+)$', blog_tag.load),
    url(r'^postList/$', blog_postList.load),
    url(r'^emailPost/$', blog_emailPost.postEmail),
    url(r'^emailPost/thanks/$', blog_emailPost.thanks),
    url(r'^user/logout/(\d+)$', blog_post.logout),
    url(r'^user/logoutcomment/$', blog_post.logoutcomment),
    url(r'^user/reg/$', blog_userReg.userReg),
    url(r'^user/regThanks/$', blog_userReg.thanks),
    url(r'^comment/$', blog_commentPost.load),
]
