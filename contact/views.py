from django.shortcuts import render
from .models import Contactform, Contactlist
# Create your views here.
def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contactformdata =Contactform(name=name, email=email, subject=subject, message=message)
        contactformdata.save()


    contactlistdata = Contactlist.objects.all()[0]
    context ={
        'contactdata': contactlistdata,
    }



    return render(request, 'contact.html', context)

