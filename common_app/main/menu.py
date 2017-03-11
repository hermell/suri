from django.core import serializers
from common_app.models import Menu

class get_menu:

    # Create your tests here.
    def top_menu(auth=None):
        top_menus = Menu.objects.filter(kind='T').order_by('ordered').values('id', 'name')
        return top_menus

    def left_menu(info=None):
        left_menus = Menu.objects.filter(kind='L', level='1').order_by('ordered', 'name').values('id', 'name', 'thumbnail', 'level', 'href_attr', 'ordered')
        sub_menus = Menu.objects.filter(kind='L', level='2').order_by('ordered', 'name').values('id', 'name', 'thumbnail', 'level', 'href_attr', 'ordered')

        return (left_menus, sub_menus,)
