from django.shortcuts import render
from .models import About
from .models import Slider
from .models import Client
# Create your views here.
def home(request):
    aboutdata = About.objects.all()[0]
    sliderdata = Slider.objects.all()
    clientdata = Client.objects.all()
    # aboutdata = About.objects.all()
    context = {
        'about' : aboutdata,
        'slider' : sliderdata,
        'client' : clientdata,
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

