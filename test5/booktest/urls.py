from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^var$', views.var),
    url(r'^label$', views.label),
    url(r'^filter$', views.filter),
    url(r'inherit$', views.inherit),
    url(r'transfer$', views.transfer),
    url(r'^fan1$', views.fan1, name='fan1'),
    url(r'^csrf$', views.csrf),
    url(r'^csrf1$', views.csrf1),
    url(r'^redirect$', views.redirect, name="fan6"),
    url(r'^fan3/(\d+)/(\d+)/$', views.redirect, name='fan3'),
    url(r'^static$', views.statics),
    url(r'^pic_upload$', views.pic_upload),
    url(r'^pic_handle$', views.pic_handle),
    url(r'^pic_show$', views.pic_show),
    url('^page(\d*)/$', views.pagelist),
    url('^area$', views.area_select),
    url('^areas$', views.areas),
]
