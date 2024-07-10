from django.shortcuts import render
from django.contrib import messages
from .models import Register

# Create your views here.
def Name (request):
    return render(request, 'Name.html')
def helloworld (request):
    return render(request, 'helloWorld.html')
def profile (request):
    return render(request, 'Profile.html')
def contacts (request):

    if request.method == 'POST':
        fname = request.POST['fname']
        email = request.POST['email']
        mssg = request.POST['mssg']

        register = Register(fname=fname, email=email, mssg=mssg)
        register.save()
        print("happy birthday")

    return render(request, 'contacts.html')
def abouts (request):
    return render(request, 'abouts.html')