from django.conf.urls import url

from mainframe_app.main.views import main_frame

urlpatterns = [
    url(r'', main_frame.init_main_frame, name='init_main'),
]