"""suriProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:', Home.as_view(), name='home')
                                Including another URLconf
                                    1. Import the include() function: from django.conf.urls import url, include
                                    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))

                                django 프로젝트에서 사용할 url을 지정
                                이 사이트의 컨텐츠 일람표 정도 된다.
                                더 자세한 사항은 상단의 urlpatterns 주소에서 확인
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]