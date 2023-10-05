from django.http import HttpResponse

def home(request):
    data = ('This is home page!')
    return HttpResponse(data)

def about(request):
    return HttpResponse('This is about page')

