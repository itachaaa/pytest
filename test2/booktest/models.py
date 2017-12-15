from django.db import models


class AreaInfo(models.Model):
    atitle = models.CharField(max_length=30)  # 名称
    aParent_id = models.ForeignKey('self', null=True, blank=True)  # 关系
