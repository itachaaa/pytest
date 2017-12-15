from django.db import models


# Create your models here.


# 定义图书类
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)  # 图书名称
    bpub_date = models.DateField()  # 发布日期
    bread = models.IntegerField(default=0)  #阅读量 默认为0
    bcomment = models.IntegerField(default=0)  # 评论量
    isDelete = models.BooleanField(default=0)  # 逻辑删除
    bremark = models.CharField(max_length=100)

    class Meta:  # 元类
        db_table = 'bookinfo'  # 指定表的名称


# 定义英雄类
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)  # 英雄名
    hgender = models.BooleanField(default=0)    # 性别
    hcontent = models.CharField(max_length=100)  # 英雄描述信息
    isDelete = models.BooleanField(default=0)    # 逻辑删除
    hbook = models.ForeignKey('BookInfo')    # 外键一对多

    class Meta:  # 元类
        db_table = 'heroinfo'
