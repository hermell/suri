from django.shortcuts import render

# Create your views here.
def go_init(request):
        return render(request, 'main/index.html', {})
def test(request):
        return render(request, 'main/sample/pages-404.html', {})
def go_main(request):
        return render(request, 'main/main.html', {})


