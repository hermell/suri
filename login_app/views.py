from django.shortcuts import render
from login_app.user import confirm_registered_user
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.
def go_login_page(request):
    return render(request, 'login_app/pages-login.html', {})


def usr_validation_chk(request):
    user_email = request.POST['user_email']
    is_registered_user = confirm_registered_user(user_email)
    # return HttpResponse(json.dumps({'name': '성공'}), content_type="application/json")
    return JsonResponse({'result': is_registered_user})
