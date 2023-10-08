from django.shortcuts import render
from .models import Contactlist
# Create your views here.
def contact(request):
    contactlistdata = Contactlist.objects.all()[0]
    context ={
        'contactdata': contactlistdata,
    }



    return render(request, 'contact.html', context)

