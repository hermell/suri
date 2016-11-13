from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.go_init, name='init'),
    url(r'main', views.go_main, name='main'),
    url(r'dash', views.test, name='404'),
]