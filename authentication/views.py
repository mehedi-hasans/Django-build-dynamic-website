from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def authlogin(request):
    if request.method=='POST':
        myusername = request.POST['username']
        mypassword = request.POST['password']
        user= authenticate(request, username = myusername, password = mypassword)
        if user is not None:
            login(request, user)
            return redirect('profile')

        else:
            print('Invalid Username or Password')

    return render(request, 'authentication/login.html')


def authlogout(request):
    logout(request)
    return redirect('login')

def authregistration(request):
    return render(request, 'authentication/registration.html')

def forgetpassword(request):
    return render(request, 'authentication/forget.html')

