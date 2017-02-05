from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext


# 404 에러 발생 시 suriProject.urls 에서 pages.views.handler404를 호출
# 404 페이지를 직접 보고 싶다면 manage.py의 debug 모드를 False로 변경
def handler404(request):
    response = render_to_response('template/sample/error/pages-404.html', {'path': request.path},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


# 404 에러 발생 시의 주석(6 Line ~ 7 Line)과 동일
def handler500(request):
    response = render_to_response('template/sample/error/pages-500.html', {'path': request.path},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

