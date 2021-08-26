from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'main.html')

def logig(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'registration.html')

def dashboard(request):
    return render(request, 'dashboard.html')
