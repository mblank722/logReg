from django.shortcuts import render, redirect
from models import User


# Create your views here.
def index(request):
    return render (request, 'log_reg/index.html')

def success(request):

    return render (request, 'log_reg/success.html')


def register(request):
    if request.method == "POST":
        print "*"*50
        print "register"

        print "req method:", request.method
        print "*"*50
        User.objects.register(request.POST)
        print 'fn:', request.POST['first_name'],\
        'ln:', request.POST['last_name'],\
        'email:', request.POST['email'],\
        'pw:', request.POST['password'],\
        'conf:', request.POST['confirm']
        print "*"*50
        return redirect("/success")

    return redirect("/")

def login(request):
    if request.method == "POST":
        print "*"*50
        print "login"
        print request.POST
        print request.method
        print "*"*50
        return redirect("/success")
    return redirect("/")
