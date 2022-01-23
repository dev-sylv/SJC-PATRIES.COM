from django.shortcuts import render
from django.core.paginator import Paginator
from Snacks_App.models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def Home(request):
    news = Blog.objects.order_by('-created')[:3]
    context = {
        'news' : news,
    }
    return render(request, 'public/frontend/index.html', context)

def About(request):
    return render(request, 'public/frontend/about.html')

def blog(request):
    most_recent = Blog.objects.order_by('created')[:2]
    blog_post = Blog.objects.order_by('-created')
    pagination = Paginator(blog_post, 6)
    page_number = request.GET.get('page')
    page_object= pagination.get_page(page_number)
    context = {
        'page_object': blog_post,
        'most_recent': most_recent,
    }
    context['page_object'] = page_object
    return render(request, 'public/frontend/blog.html', context)

def Blog_single(request):
    return render(request, 'public/frontend/blog-single.html')

def Contact(request):
    return render(request, 'public/frontend/contact.html')

def Menu(request):
    snack = Snacks.objects.all()
    return render(request, 'public/frontend/menu.html', {'snack': snack})

def Services(request):
    return render(request, 'public/frontend/services.html')

def Login(request):
    return render(request, 'public/frontend/Login.html')

def Signup(request):
    return render(request, 'public/frontend/Signup.html')

def Order(request):
    return render(request, 'public/frontend/order.html')









