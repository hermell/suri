from django.shortcuts import render
from django.http import JsonResponse
from common_app.main.menu import get_menu

class main_frame:

    # url에서 받아올 때 괄호를 사용한 정규식이 있다면 argument를 두개 받는 메소드를 생성해야 함
    def menu(request):
        top_menus = main_frame.top_menu()
        left_menus = main_frame.left_menu()
        return render(request, 'main.html', {'top_menus': top_menus,'left_menus':left_menus})

    def coming_soon(request):
        return render(request, 'extras-coming-soon.html')


    def top_menu(top_info=None):
        top_menus = get_menu.top_menu()
        return top_menus

    def left_menu(left_info=None):
        total_left_menus = get_menu.left_menu()
        left_menus = total_left_menus[0]
        sub_menus = total_left_menus[1]
        left_menu_dict = dict((left_menu['ordered'], left_menu) for left_menu in left_menus)

        for sub_menu in sub_menus:

            ordered = sub_menu['ordered']
            if 'sub_menus' in left_menu_dict[ordered]:
                left_menu_dict[ordered]['sub_menus'].append(sub_menu)
            else:
                left_menu_dict[ordered]['sub_menus'] = [sub_menu]

        return list(left_menu_dict.values())