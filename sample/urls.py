from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'index', views.go_init, name='index'),
    url(r'main', views.go_main, name='main'),
    url(r'dash', views.test, name='404'),
    url(r'', views.go_others, name='others'),
]