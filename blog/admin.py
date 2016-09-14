from django.contrib import admin
from blog.models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'updateDatetime', 'createDatetime')  # 列表显示
    search_fields = ('title','body')  # 搜索
    list_filter = ('title',)  # 过滤器
    date_hierarchy = 'updateDatetime'  # 日期型字段进行层次划分。
    ordering = ('-updateDatetime',)  # 对修改日期降序排列，可以在增加默认为升序
    #fields = ('name', 'sex', 'age', 'birth', 'type')  # 自定义编辑表单，在编辑表单的时候 显示哪些字段，显示的属性
    #date_hierarchy = 'updateDatetime'  # 另外一种过滤日期的方式   增加这行 点击年的时候会报错

admin.site.register(Post,PostAdmin)
admin.site.register(Tag)