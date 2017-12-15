from django.db import models


# Create your models here.


class BookInfoManager(models.Manager):
    def total(self):
        return super().all().filter(isDelete=0)

    def shuminghao(self, obj):
        for i in obj:
            i.btitle = "《%s》" % i.btitle
        return obj


# 定义图书模型类BookInfo
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)  # 图书名称
    bpub_date = models.DateField()  # 发布日期
    bread = models.IntegerField(default=0)  # 阅读量，默认值表示在创建模型对象时，不指定这个属性值，这个值就为0
    bcommet = models.IntegerField(default=0)  # 评论量
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    bremark = models.CharField(max_length=100, null=True)

    objects = BookInfoManager()

    class Meta:  # 元信息类
        db_table = 'bookinfo'  # 指定表的名称


# 定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)  # 英雄姓名
    hgender = models.BooleanField(default=True)  # 英雄性别
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    hcontent = models.CharField(max_length=100)  # 英雄描述信息
    hbook = models.ForeignKey('BookInfo')  # 英雄与图书表的关系为一对多，所以属性定义在英雄模型中
    # 上一句中 BookInfo 加不加引号都可以


class AreaInfo(models.Model):
    atitle = models.CharField(max_length=30)  # 名称
    aParent = models.ForeignKey('self', null=True, blank=True)  # 关系
