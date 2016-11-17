from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2> webapp is ready!</h2>")