from django.shortcuts import render
from django.http      import HttpResponse

## First View
def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context = context_dict)

## Second View
def about(request):
    return HttpResponse('This is the about page')
