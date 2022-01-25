from django.shortcuts import render
from django.core.paginator import Paginator
from Snacks_App.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# Create your views here.
def Home(request):
    news = Blog.objects.order_by('-created')[:3]
    context = {
        'news' : news,
    }
    return render(request, 'public/frontend/index.html', context)

def About(request):
    team = Team.objects.all()
    return render(request, 'public/frontend/about.html', {'team': team})

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
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        # phone= request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # get_menu = Menu.objects.get(menu_id__id)
        submit_data = ContactMe(name=name, email=email, subject=subject, message=message)
        submit_data.save()
        messages.success(request, 'Hello dear, thank you for your message! Message sent successfully')
    return render(request, 'public/frontend/contact.html')

def snacks(request):
    snack = Menu.objects.order_by('created')[:3]
    return render(request, 'public/frontend/menu.html', {'snack': snack})

def Services(request):
    return render(request, 'public/frontend/services.html')

def Login(request):
    return render(request, 'public/frontend/Login.html')

def Signup(request):
    return render(request, 'public/frontend/Signup.html')

def Order(request):
    return render(request, 'public/frontend/order.html')









