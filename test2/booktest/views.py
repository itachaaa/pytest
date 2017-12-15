from django.shortcuts import render
from django.http import HttpResponse
from booktest.models import BookInfo, HeroInfo, AreaInfo
from django.db.models import F, Q
from django.db.models import Sum, Count, Max, Min, Avg

# Create your views here.


def index(request):
    return HttpResponse("hello world")


def booklist(request):
    # 1. 获取所有图书
    books1 = BookInfo.objects.all().order_by("-bremark", "-id")
    books1 = BookInfo.objects.shuminghao(books1)
    # 2. 获取没有逻辑删除的图书
    books2 = BookInfo.objects.total()
    # 3. 获取id值为3的图书
    # books3 = BookInfo.objects.filter(id__exact=1)
    books3 = BookInfo.objects.filter(id=1)
    # 4. 获取包含"射"
    books4 = BookInfo.objects.filter(bpub_date__contains="1986-07-24")
    # 5. 获取备注不为空的图书
    books5 = BookInfo.objects.filter(bremark__isnull=False)
    # 6. 获取id是1或者3的图书
    books6 = BookInfo.objects.filter(id__in=[1, 3])
    # 9. 获取id不为3的图书
    books9 = BookInfo.objects.exclude(id=3)
    # 10. 获取评论量大于阅读量的图书
    books10 = BookInfo.objects.filter(bread__gte=F('bcommet'))
    # 11. 获取阅读量大于30 且 id大于等于3
    books11 = BookInfo.objects.filter(Q(id__gt=3) & Q(bread__gt=30))
    # 13. 聚合函数
    books13 = BookInfo.objects.aggregate(Avg("id")).get('id__avg')
    books131 = BookInfo.objects.count()
    # 14. 图书中的英雄包含八
    books14 = BookInfo.objects.filter(heroinfo__hcontent__contains="八")
    a = []
    for book in books14:
        a.append(book.heroinfo_set.filter(hcontent__contains="八"))
    c = a[0][0]
    b = a[1][0]
    # a = [b, c]
    # 15. 自关联

    context = {
        'books1': books1,
        'books2': books2,
        'books3': books3,
        'books4': books4,
        'books5': books5,
        'books6': books6,
        'books9': books9,
        'books10': books10,
        'books11': books11,
        'books13': books13,
        'books131': books131,
        'books14': books14,
        "a": a,
        "b": b,
        "c": c
    }
    return render(request, 'booktest/booklist.html', context)


def area(request):
    area = AreaInfo.objects.get(pk=440100)
    return render(request, 'booktest/area.html', {'area': area})
