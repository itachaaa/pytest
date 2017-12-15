from django.db import models


class PicTest(models.Model):
    pic = models.ImageField(upload_to='booktest/')


# 定义图书模型类BookInfo
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)  # 图书名称
    bpub_date = models.DateField()  # 发布日期
    bread = models.IntegerField(default=0)  # 阅读量，默认值表示在创建模型对象时，不指定这个属性值，这个值就为0
    bcommet = models.IntegerField(default=0)  # 评论量
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    bremark = models.CharField(max_length=100, null=True)

    class Meta:  # 元信息类
        db_table = 'bookinfo'  # 指定表的名称


class AreaInfo(models.Model):
    # atitle = models.CharField(max_length=30)  # 名称
    aParent = models.ForeignKey('self', null=True, blank=True)  # 关系

    def title(self):
        return self.atitle

    title.admin_order_field = 'atitle'
    title.short_description = '区域名称'

    def parent(self):
        return self.aParent.atitle

    parent.short_description = '父级区域名称'

    atitle = models.CharField('标题', max_length=30)  # 名称

    def __str__(self):
        return self.atitle
