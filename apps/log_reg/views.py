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
        if register['insertIsValid']:
            print "*"*50
            print "view: Register Method - Success"
            print "req method:", request.method
            print "*"*50
            print 'fn:', request.POST['first_name'],\
            'ln:', request.POST['last_name'],\
            'email:', request.POST['email'],\
            'pw:', request.POST['password'],\
            'conf:', request.POST['confirm']
            print "*"*50
            print "register:", register
            request.session['id']=register['id']
            request.session['first_name']=request.POST['first_name']
            print "request.session:",  request.session['id']
            return render (request, 'log_reg/success.html')
        else:
            for error in register['errors']:
                messages.error(request, error)
            print "*"*50
            print "view: Register Method - Errors"
            print "req method:", request.method
            print "*"*50
            print 'fn:', request.POST['first_name'],\
            'ln:', request.POST['last_name'],\
            'email:', request.POST['email'],\
            'pw:', request.POST['password'],\
            'conf:', request.POST['confirm']
            print "*"*50
    return redirect("/")


def login(request):
    if request.method == "POST":
        login = User.objects.login(request.POST)
        if login['insertIsValid']:
            print "*"*50
            print "view: Login Method - Success"
            print "req method:", request.method
            print "*"*50
            print 'id:' , request.session['id'], \
            'email:', request.POST['email'], \
            'pw:', request.POST['password']

            print "*"*50
            print "login:", login
            request.session['id']=login['id']
            print "request.session:",  request.session['id']
            return render (request, 'log_reg/success.html')
        else:
            for error in register['errors']:
                messages.error(request, error)
            print "*"*50
            print "view: Register Method - Errors"
            print "req method:", request.method
            print "*"*50
            print 'fn:', request.POST['first_name'],\
            'ln:', request.POST['last_name'],\
            'email:', request.POST['email'],\
            'pw:', request.POST['password'],\
            'conf:', request.POST['confirm']
            print "*"*50
    #     print "*"*50
    #     print "login"
    #     print request.POST
    #     print request.method
    #     print "*"*50
    #     print 'ID:', request.POST['confirm']
    #     print 'Email:',  request.POST['email']
    #     print 'PW:' , request.POST['password']
    #     return redirect("/success")
    # return redirect("/")
