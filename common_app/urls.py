from django.conf.urls import url

from common_app.main.views import main_frame

urlpatterns = [
    url(r'left_menu_list', main_frame.left_menu, name='left_menu'),
    url(r'coming_soon', main_frame.coming_soon, name='coming_soon'),
    url(r'', main_frame.menu, name='top_menu'),
]