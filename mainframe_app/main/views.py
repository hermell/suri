from django.shortcuts import render

class main_frame:

    # url에서 받아올 때 괄호를 사용한 정규식이 있다면 argument를 두개 받는 메소드를 생성해야 함
    def init_main_frame(request):
        return render(request, 'main.html', {'aa':'aaaaaaaa'})


