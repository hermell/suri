from django.conf.urls import url

from user_app.login.views import usr_dupl_chk, usr_management

urlpatterns = [
    url(r'^(\w)*validation_chk', usr_dupl_chk.usr_duplication_chk, name='login'),
    url(r'^user(\w)*', usr_management.usr_insert, name='login'),
]