from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def employee(request):
    return HttpResponse('This is the emloyee page')

def profile(request):
    return render(request, 'employee/profile.html')