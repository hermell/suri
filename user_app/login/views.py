import re

from django.http import JsonResponse
from django.shortcuts import render

from user_app.login.user import confirm_registered_info


# Create your views here.
def go_login_page(request):
    return render(request, '../template/login/pages-login.html', {})

class usr_dupl_chk:

    # url에서 받아올 때 괄호를 사용한 정규식이 있다면 argument를 두개 받는 메소드를 생성해야 함
    def usr_duplication_chk(request, split_char):

        #request.path의
        chk_info = re.sub("/(\w)*/", "",request.path).replace("_validation_chk","")
        # result = None

        # if chk_info == "email":
        result = confirm_registered_info(chk_info, request.POST[chk_info])
        # elif chk_info == "nickname":
        #     result = confirm_registered_info('nickname', request.POST['nickname'])
        # else:
        #     result = False

        return JsonResponse({'result': result})
