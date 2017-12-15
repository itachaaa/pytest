from django.contrib import admin
from .models import AreaInfo
from .models import PicTest


# 以块的形式嵌入
class AreaStackedInline(admin.StackedInline):
    model = AreaInfo  # 关联子对象
    extra = 2  # 额外编辑2个子对象


# 以表格的形式嵌入
class AreaTabularInline(admin.TabularInline):
    model = AreaInfo  # 关联子对象
    extra = 2  # 额外编辑2个子对象


class AreaAdmin(admin.ModelAdmin):
    list_per_page = 10
    # actions_on_top = False
    # actions_on_bottom = True
    list_display = ['id', 'atitle', 'title', 'parent']  # 列表页显示内容
    list_filter = ['atitle']  # 以一个标签为过滤器
    search_fields = ['atitle']  # 以一个标签为搜索框
    # fields = ['atitle', 'aParent']   # 编辑页面, 显示的内容, 先后也会有区别

    fieldsets = (
        ('基本', {'fields': ['atitle']}),
        ('高级', {'fields': ['aParent']})
    )    # 分组显示

    # inlines = [AreaStackedInline]
    inlines = [AreaStackedInline, AreaTabularInline]  # 表示在模型的编辑页面嵌入关联模型的编辑


admin.site.register(PicTest)
