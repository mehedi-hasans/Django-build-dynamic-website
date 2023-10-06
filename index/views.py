from django.shortcuts import render
from .models import About
from .models import Slider
# Create your views here.
def home(request):
    aboutdata = About.objects.all()[0]
    sliderdata = Slider.objects.all()
    # aboutdata = About.objects.all()
    context = {
        'about' : aboutdata,
        'slider' : sliderdata,
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

