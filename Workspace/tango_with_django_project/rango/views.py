from django.shortcuts import render
from django.http      import HttpResponse

## Index View
def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context = context_dict)

## About View
def about(request):
    return HttpResponse('This is the about page')

## Users
def users(request):
    context_dict = {'username': 'Luis'}
    return render(request, 'rango/users.html', context = context_dict)
