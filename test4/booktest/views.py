from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from booktest.models import BookInfo, HeroInfo


def index(request, para2, para1):
    context = {'v1': para1, 'v2': para2}
    return render(request, 'booktest/index.html', context)


def get(request):
    dict_get = request.GET
    a = dict_get.getlist("a")
    b = dict_get.get("b")

    context = {'a': a, 'b': b}
    return render(request, 'booktest/get.html', context)


def wish(request):
    dict = request.GET
    name = dict.get('name')
    list = dict.getlist('a')
    textlist = ['生日快乐', '节日快乐', '学习进步', '四季发财']
    str = ''
    for i in list:
        str += textlist[int(i)] + "    "

    context = {'name': name, 'wish': str}
    return render(request, 'booktest/wish.html', context)


def post(request):
    if request.method == 'GET':
        return render(request, 'booktest/post.html')
    elif request.method == 'POST':
        dict_post = request.POST
        username = dict_post.get('username')
        password = dict_post.get('password')
        gender = dict_post.get('gender')
        hobby = dict_post.getlist('hobby')  # 一键多值
        context = {
            'name': username,
            'pwd': password,
            'gender': gender,
            'hobby': hobby
        }
        return render(request, 'booktest/post1.html', context)


# 定义视图 返回包含ajax程序的模板
def json(request):
    return render(request, "booktest/json.html")


# 定义视图, 返回json 数据
def json1(request):
    books = BookInfo.objects.all()
    lists = []
    for book in books:
        lists.append({'btitle': book.btitle, 'bpub_date': book.bpub_date},)

    return JsonResponse({'lists': lists})


# 重定向
def red(request):
    return HttpResponseRedirect("get")


# cookies设置
def set_cookie(request):
    response = HttpResponse("set cookies")
    response.set_cookie('mark', 'hello', max_age=3600*6)
    return response


def get_cookie(request):
    cookie = request.COOKIES['mark']
    return HttpResponse(cookie)


# 设置session
def session(request):
    request.session['username'] = 'Tom'
    return HttpResponse("设置session")


# 获取session
def get_session(request):
    s1 = request.get_session("username")
    return HttpResponse(s1)


# 获取path
def path(request):
    return HttpResponse(request.path)


# 获取method
def method(request):
    return HttpResponse(request.method)
