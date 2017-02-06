from django.shortcuts import render, redirect
from django.contrib import messages
from models import User

# Create your views here.
def index(request):
    return render (request, 'log_reg/index.html')

def success(request):
    return render (request, 'log_reg/success.html')

def register(request):
    if request.method == "POST":
        register = User.objects.register(request.POST)
        if register['registerIsValid']:
            request.session['id']=register['id']
            request.session['first_name']=request.POST['first_name']
            request.session['operation']=register['operation']
            return render (request, 'log_reg/success.html')
        else:
            for error in register['errors']:
                messages.error(request, error)
    return redirect("/")


def login(request):
    if request.method == "POST":
        login = User.objects.login(request.POST)
        if login['loginIsValid']:
            request.session['operation'] = login['operation']
            return render (request, 'log_reg/success.html')
        else:
            for error in login['errors']:
                messages.error(request, error)

    return redirect("/"
