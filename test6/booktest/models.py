from django.db import models


class AreaInfo(models.Model):
    atitle = models.CharField('标题', max_length=30)  # 名称
    aParent = models.ForeignKey('self', null=True, blank=True)  # 关系
