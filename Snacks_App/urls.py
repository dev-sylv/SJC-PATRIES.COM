from django.urls import path
from Snacks_App import views

app_name = 'Snacks_App'


urlpatterns = [
    path('about/', views.About, name='About'),
    path('blog-single-page/', views.Blog_single, name='Blog_single'),
    path('blog-page/', views.blog, name='Blog'),
    path('contact-us/', views.Contact, name='Contact'),
    path('menu-page/', views.snacks, name='Menu'),
    path('snack-detail/<slug:my_slug>/', views.snacks_details, name='snacks_details'),
    path('services/', views.Services, name='Services'),
    path('Login/', views.login_user, name='Login'),
    path('Logout/', views.Logout_user, name='Logout'),
    path('register/', views.Register, name='register'),
    path('order/', views.Order, name='Order'),
    path('form/', views.Myform, name='Myform'),
    path('dashboard/', views.User_dashboard, name='Udashboard'),
]