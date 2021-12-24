from django.urls import path
from Snacks_App import views

app_name = 'Snacks_App'


urlpatterns = [
    path('about/', views.About, name='About'),
    path('blog-single-page/', views.Blog_single, name='Blog_single'),
    path('blog-page/', views.Blog, name='Blog'),
    path('contact-us/', views.Contact, name='Contact'),
    path('menu-page', views.Menu, name='Menu'),
    path('services/', views.Services, name='Services'),
    path('Login/', views.Login, name='Login'),
    path('Signup/', views.Signup, name='Signup'),



]