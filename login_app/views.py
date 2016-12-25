from django.shortcuts import render

# Create your views here.
# Create your views here.
def go_login_page(request):
    return render(request, 'login_app/pages-login.html', {})
