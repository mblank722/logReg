from django.shortcuts import render redirect

# Create your views here.
def index(request):
    return render (request, 'log_reg/index.html')

def success(request):
    return render (request, 'log_reg/success.html')
