from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from Snacks_App.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.conf import settings

from Snacks_App.forms import *
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



# Create your views here.
def Home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneNo = request.POST.get('phoneNo')
        message = request.POST.get('message')
        submit_data = ContactUs(name=name, email=email, phonenumber=phoneNo, note=message)
        submit_data.save()
        messages.success(request, 'Message Sent Successfully. Thank you for sending us a message')

    news = Blog.objects.order_by('-created')[:3]
    pastry = Menu.objects.order_by('-created')[:3]
    pastries = Menu.objects.order_by('-created')[4:7]
    price = Menu.objects.order_by('-created')[:4]
    pricing = Menu.objects.order_by('-created')[5:]
    
    context = {
        'news' : news,
        'pastry': pastry,
        'pastries': pastries,
        'price': price,
        'pricing': pricing,
    }
    return render(request, 'public/frontend/index.html', context)

def About(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneNo = request.POST.get('phoneNo')
        message = request.POST.get('message')
        submit_data = ContactUs(name=name, email=email, phonenumber=phoneNo, note=message)
        submit_data.save()
        messages.success(request, 'Message Sent Successfully. Thank you for sending us a message')

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
        phones = request.POST.get('phones')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # get_menu = Menu.objects.get(menu_id__id)

        subject = 'From Success Jutonia Cakes and Pastries Site'
        context = {
            'name': name,
            'email': email,
            'phones': phones,
            'message': message,
        }
        html_message = render_to_string('public/frontend/mail-template.html', context)
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        send = mail.send_mail(subject, plain_message, from_email, ['nicsylvia15f@gmail.com',], html_message=html_message, fail_silently=True)
        if send:
            submit_data = ContactMe(name=name, email=email, phones=phones, subject=subject, message=message)
            submit_data.save()
            messages.success(request, 'Hello dear, thank you for your message! Message sent successfully')
        else:
            messages.error(request, 'An Error Occured! Please Make Sure you have Internet Connection')
    return render(request, 'public/frontend/contact.html')

def snacks(request):
    snack = Menu.objects.order_by('created')[2:5]
    snacky = Menu.objects.order_by('created')[6:]
    priceA = Food.objects.order_by('created')[:3]
    priceB = Cakes.objects.order_by('created')[:3]
    context = {
        'snack': snack,
        'snacky': snacky,
        'pricea': priceA,
        'priceb': priceB,
    }
    return render(request, 'public/frontend/menu.html', context)

def snacks_details(request, my_slug):
    menu_detail = Menu.objects.get(slug=my_slug)
    context = {
        'details': menu_detail,
    }
    return render(request, 'public/frontend/menu-details.html', context)

def Services(request):
    meal = Menu.objects.order_by('created')[:2]
    parfait = Menu.objects.order_by('created')[4:6]
    context = {
        'meal': meal,
        'parfait': parfait,
    }
    return render(request, 'public/frontend/services.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Snacks_App:Udashboard')
        else:
            messages.error(request, 'Username and password do not match. Please recheck and input the correct details')
            return redirect('Snacks_App:Login')
    return render(request, 'public/frontend/Login.html')

def Logout_user(request):
    logout(request)
    return redirect('Snacks_App:Login')

def Register(request):
    register_form = RegisterForm()
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'You Registered Successfully, Welldone ')
        else:
            register_form = RegisterForm()
    return render(request, 'public/frontend/register.html',{'sylvia':register_form})
    # 1:16:00 in video

def Order(request):
    return render(request, 'public/frontend/order.html')

def Myform(request):
    submit_data = Myform()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneNo = request.POST.get('phoneNo')
        message = request.POST.get('message')
        # if send:
        submit_data = ContactUs(username=name, email=email, phonenumber=phoneNo, message=message)
        submit_data.save()
        messages.success(request, 'Message Sent Successfully. Thank you for sending us a message')
        # else:
        #     messages.error(request, 'An error occured')
    return render(request, 'public/frontend/myform.html')

    
@login_required(login_url='/snacks/Login/')
def User_dashboard(request):
    return render(request, 'public/frontend/user-dashboard.html')

