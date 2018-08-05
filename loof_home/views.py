from django.http import HttpResponse


def index(request):
    return HttpResponse('Empty page, try <a href="/mat/">here</a>')
