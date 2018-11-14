from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Dmytro! This is the index page")
