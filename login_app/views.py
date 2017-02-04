from django.shortcuts import render
from login_app.user import confirm_registered_info
from django.http import JsonResponse
import re
from django.http import HttpResponse


# Create your views here.
def go_login_page(request):
    return render(request, 'login_app/pages-login.html', {})

class usrDuplChk:
    # url에서 받아올 때 괄호를 사용한 정규식이 있다면 argument를 두개 받는 메소드를 생성해야 함
    def usr_duplication_chk(request, split_char):
        chk_info = re.sub("/(\w)*/", "",request.path).replace("_validation_chk","")
        result = None
        print(chk_info)

        if chk_info == "email":
            result = confirm_registered_info('email', request.POST['user_email'])
        elif chk_info == "nickname":
            result = confirm_registered_info('nickname', request.POST['nickname'])
        else:
            result = False

        return JsonResponse({'result': result})
