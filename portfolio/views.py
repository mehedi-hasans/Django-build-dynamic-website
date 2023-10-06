from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    text = {
        'name' : "Mehedi Hasan",
        'department' : "Computer",
        'phone' : 56551515,
        'friend' : ['Sakib', 'Hasan', 'Tamin', 'Liton Das']
    }

    return render(request, 'index.html', text)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

