from django.db import models

class Post(models.Model):
    '''存储blog的主表'''
    title = models.CharField(u'标题',max_length = 200)
    body = models.TextField(u'内容')  # 也可以写做 verbose_name=u'内容'
    createDatetime = models.DateTimeField(u'创建时间',auto_now_add = True)
    updateDatetime = models.DateTimeField(u'修改时间',auto_now = True)
    tag = models.ManyToManyField('Tag')
    class Meta:
        app_label = 'blog'  #应用的名字，必须添加 ， __init__.py 中 要添加本类的 import
        #db_table = 'blog_post'  # 数据库名
        verbose_name = u'博客'  # 修改从管理级'博客'进入后的页面显示，显示为'博客'
        verbose_name_plural = u'博客'  # 修改管理级页面显示
    def __str__(self):
        return self.title

class Tag(models.Model):
    '''存储tag的表'''
    name = models.CharField(u'名字', max_length= 200)
    class Meta:
        app_label = 'blog'
        verbose_name = u'标签'
        verbose_name_plural = u'标签'
    def __str__(self):
        return self.name