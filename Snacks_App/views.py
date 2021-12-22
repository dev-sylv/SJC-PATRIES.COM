from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, 'public/frontend/index.html')

def About(request):
    return render(request, 'public/frontend/about.html')


