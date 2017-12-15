from django.conf.urls import include, url
from booktest import views

urlpatterns = [
    url(r'^(?P<para1>\d+)/(?P<para2>\d+)$', views.index),
    url(r'^get$', views.get),
    url(r'^wish$', views.wish),
    url(r'^post$', views.post),
    url(r'^json$', views.json),
    url(r'^json1$', views.json1),
    url(r"^red$", views.red),
    url(r"set_cookie$", views.set_cookie),
    url(r"get_cookie$", views.get_cookie),
    url(r"^session$", views.session),
    url(r"^get_session$", views.session),
    url(r"path", views.path),
    url(r"method", views.method)
]

