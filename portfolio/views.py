from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')
    # data = ('This is home page!')
    # return HttpResponse(data)

def about(request):
    return HttpResponse('This is about page')

