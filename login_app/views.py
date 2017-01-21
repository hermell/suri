from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render
from login_app.tests import test
from django.http import JsonResponse

# Create your views here.
def go_login_page(request):
    return render(request, 'login_app/pages-login.html', {})
def create_user(request):
    # test()
    # return HttpResponse(json.dumps({'name': '성공'}), content_type="application/json")
    return JsonResponse({'name': '성공'})
