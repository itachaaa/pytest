from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^area_select$', views.area_select),
    url(r'^areas$', views.areas),

]
