from django.shortcuts import render
from django.http import HttpResponse
from booktest.models import BookInfo, HeroInfo
# Create your views here.


def index(request):
    return HttpResponse("Hello World!")


def booklist(request):
    books = BookInfo.objects.all()
    return render(request, 'booktest/booklist.html', {'books': books})
