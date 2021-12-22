from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'public/frontend/index.html')

def About(request):
    return render(request, 'public/frontend/about.html')

def Blog(request):
    return render(request, 'public/frontend/blog.html')

def Blog_single(request):
    return render(request, 'public/frontend/blog-single.html')

def Contact(request):
    return render(request, 'public/frontend/contact.html')

def Menu(request):
    return render(request, 'public/frontend/menu.html')

def Services(request):
    return render(request, 'public/frontend/services.html')







