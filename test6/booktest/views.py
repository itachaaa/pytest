from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from booktest.models import AreaInfo
from booktest import models


# 省市区控制
def area_select(request):
    return render(request, 'booktest/area_s.html')


def areas(request):
    parent = request.GET.get('parent')
    if parent == 'None':
        areas = AreaInfo.objects.filter(aParent=None)
    else:
        areas = models.AreaInfo.objects.filter(aParent=parent)

    jsonstr = []
    for area in areas:
        jsonstr.append({'id': area.id, 'atitle': area.atitle, 'aparent': area.aParent_id})

    return JsonResponse({'list': jsonstr})
