from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import BookInfo, PicTest, AreaInfo
from booktest import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.paginator import Paginator


def var(request):
    dict = {'title': '字典键值'}
    book = BookInfo.objects.all()
    print(book)
    # book.btitle = '对象属性'
    context = {'dict': dict, 'book': book}
    return render(request, 'booktest/var.html', context)


# 标签用法
def label(request):
    context = {'list': BookInfo.objects.all()}
    return render(request, 'booktest/label.html', context)


# 自定义过滤器
def filter(request):
    context = {'list': BookInfo.objects.all()}
    return render(request, 'booktest/filter.html', context)


# html 文件里面load filters时, 其文件名不能和别的文件重名, 否则导入会出错


# 继承
def inherit(request):
    context = {'title': "继承", 'list': BookInfo.objects.all()}
    return render(request, 'booktest/inherit.html', context)


# 转义
def transfer(request):
    context = {'content': '<h1>hello world</h1>'}
    return render(request, 'booktest/transfer.html', context)


# 反向解析
def fan1(request):
    return render(request, 'booktest/fan1.html')


# csrf验证
def csrf(request):
    return render(request, 'booktest/csrf.html')


# 处理POST请求
def csrf1(request):
    dict = request.POST
    uname = dict.get('uname')
    money = dict.get('money')

    # 获取csrf验证码
    token = dict.get('csrfmiddlewaretoken')

    str = '%s--%s--%s' % (uname, money, token)
    return HttpResponse(str)


'''
# 图形验证码
def verify(request):
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 200
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]

    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    font = ImageFont.truetype('FreeMono.ttf', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw

    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')
'''


# 反向解析 超链接
# def redirect(request):
#     return HttpResponseRedirect(reverse('booktest:fan1'))


def redirect(request):
    return HttpResponseRedirect(reverse('booktest:fan3', args=(18, 188)))


# 静态文件加载
def statics(request):
    return render(request, 'booktest/statics.html')


# 自定义上传图片
def pic_upload(request):
    return render(request, 'booktest/pic_upload.html')


def pic_handle(requeest):
    f1 = requeest.FILES.get('pic')
    fname = '%s/booktest/%s' % (settings.MEDIA_ROOT, f1.name)
    with open(fname, 'wb') as pic:
        for c in f1.chunks():
            pic.write(c)
    Pic = PicTest()
    Pic.pic = fname
    Pic.save()
    #  通过创建models 类的对象, 可以实现在python中操作数据库的数据, 就像 shell 一样
    return HttpResponse('ok')


# 显示图片
def pic_show(request):
    pic = PicTest.objects.all()
    context = {'pic': pic}
    return render(request, 'booktest/pic_show.html', context)


# 分页
def pagelist(request, pindex):
    sheng = AreaInfo.objects.filter(aParent__isnull=True)
    paginator = Paginator(sheng, 10)
    if pindex == "":
        pindex = 1
    page = paginator.page(pindex)
    return render(request, 'booktest/pagelist.html', {'page': page})


# 省市区控制
def area_select(request):
    return render(request, 'booktest/area_select.html')


def areas(request):
    parent = request.GET.get('parent')
    if parent == 'None':
        print(1111)
        areas_province = AreaInfo.objects.filter(aParent_id=990000)
        print("----areas", areas_province)
    else:
        print("----else:", parent)
        areas = models.AreaInfo.objects.filter(aParent_id=int(parent))
    jsonstr = []
    for area in areas:
        jsonstr.append({'id': area.id, 'atitle': area.atitle, 'aparent': area.aParent_id})
    print("----jsonstr:", jsonstr)
    return JsonResponse({'list': jsonstr})
