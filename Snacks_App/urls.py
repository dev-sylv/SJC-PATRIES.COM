from Snacks_App import views
from django.urls import path

urlpatterns = [
    path('about-us', views.About, name='About'),
]