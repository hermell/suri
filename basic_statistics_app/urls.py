from django.conf.urls import url

from basic_statistics_app.dictionary import views

urlpatterns = [
    url(r'mean', views.mean.init, name='mean'),
]