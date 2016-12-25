from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def go_init(request):
    return render(request, 'index.html', {})

def go_others(request):

    print(request.path)

    original_path = request.path
    modefied_path = ''
    path_length = original_path.__len__()

    # admin 페이지에서 오른쪽 상단의 view_site라는 문구 클릭 시 url 패턴이 ""로 들어옴
    # 이 경우 index.html로 들어가도록 변경
    # 디버깅 결과 url 패턴이 ""로 들어오는 경우의 __len__ = 1 임
    # 왜인지는 아직 모름..ㅠㅠ
    # 일단 디버깅 결과를 토대로 아래와 같이 if문 작성
    if path_length > 1:
        modefied_path = original_path[1:path_length]
    else:
        modefied_path = "index.html"

    return render(request, modefied_path, {})

# 404 에러 발생 시 suriProject.urls 에서 pages.views.handler404를 호출
# 404 페이지를 직접 보고 싶다면 manage.py의 debug 모드를 False로 변경
def handler404(request):
    response = render_to_response('error_pages/pages-404.html', {'path': request.path},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


# 404 에러 발생 시의 주석(6 Line ~ 7 Line)과 동일
def handler500(request):
    response = render_to_response('error_pages/pages-500.html', {'path': request.path},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response