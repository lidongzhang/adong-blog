from django.db import models

class User(models.Model):
    '''存储用户信息'''
    name = models.CharField('姓名', max_length = 50)
    nickname_email = models.CharField('用户名',max_length = 200)
    password = models.CharField('密码', max_length =200)
    ismember = models.BooleanField('记住用户')
    createDatetime = models.DateTimeField(u'创建时间',auto_now_add = True)
    updateDatetime = models.DateTimeField(u'修改时间',auto_now = True)
    class Meta:
        app_label = 'blog'
        verbose_name = '用户'
        verbose_name_plural = '用户'
    def __str__(self):
        return self.name


class Post(models.Model):
    '''存储blog的主表'''
    title = models.CharField(u'标题',max_length = 200)
    body = models.TextField(u'内容')  # 也可以写做 verbose_name=u'内容'
    createDatetime = models.DateTimeField(u'创建时间',auto_now_add = True)
    updateDatetime = models.DateTimeField(u'修改时间',auto_now = True)
    tag = models.ManyToManyField('Tag')
    count = models.IntegerField(default=0)
    class Meta:
        app_label = 'blog'  #应用的名字，必须添加 ， __init__.py 中 要添加本类的 import
        #db_table = 'blog_post'  # 数据库名
        verbose_name = u'博客'  # 修改从管理级'博客'进入后的页面显示，显示为'博客'
        verbose_name_plural = u'博客'  # 修改管理级页面显示
    def __str__(self):
        return self.title

class PostComment(models.Model):
    '''post评论'''
    postID = models.ForeignKey(Post)
    content = models.CharField(max_length=1000)
    userID = models.ForeignKey(User)
    createDatetime = models.DateTimeField(auto_now = True)
    class Meta:
        app_label = 'blog'

class Comment(models.Model):
    '''网站留言'''
    content = models.CharField(max_length = 1000)
    userID = models.ForeignKey(User)
    createDatetime = models.DateTimeField(auto_now = True)
    class Meta:
        app_label = 'blog'
    
class Tag(models.Model):
    '''存储tag的表'''
    name = models.CharField(u'名字', max_length= 200)
    class Meta:
        app_label = 'blog'
        verbose_name = u'标签'
        verbose_name_plural = u'标签'
    def __str__(self):
        return self.name

class Hit(models.Model):
    '''首页点击数'''
    count = models.IntegerField()
    

