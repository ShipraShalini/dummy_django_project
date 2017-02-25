from django.http import HttpResponse

def hello(request):
    return HttpResponse('Hello')

def helloname(request, name='Stranger'):
    return HttpResponse('Hello' + " " + name +"!")
