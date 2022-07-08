from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print(request)
    return HttpResponse('fall i will follow')
def test(request):
    return HttpResponse('fuck')