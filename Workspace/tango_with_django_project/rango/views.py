from django.shortcuts import render
from django.http      import HttpResponse

## First View
def index(request):
    return HttpResponse('Rango says hi!')

## Second View
def about(request):
    return HttpResponse('This is the about page')
