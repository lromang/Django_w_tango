from django.shortcuts import render
from django.http      import HttpResponse

## First view
def index(request):
    return HttpResponse('Rango says hi!')
