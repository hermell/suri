from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def go_login_page(request):
    return render(request, 'login_app/pages-login.html', {})
def create_user(request):
    # test()
    # return HttpResponse(json.dumps({'name': '성공'}), content_type="application/json")
    print("debug: " + request.POST.get('email'))
    return JsonResponse({'name': '성공'})
