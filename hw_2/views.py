from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Добро пожаловать в HW_2 API</h1><p>Используйте <a href='/movies/'>/movies/</a> или <a href='/articles/'>/articles/</a></p>")
