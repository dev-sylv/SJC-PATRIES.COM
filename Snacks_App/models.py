from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    Firstname = models.CharField(max_length=20)
    Lastname = models.CharField(max_length=20)
    Username = models.CharField(max_length=15)
    slug = models.SlugField(unique=True)
    password = models.CharField(max_length=10)
    profile_image = models.ImageField(blank=True, null=True, upload_to='uploads/')
    email = models.EmailField(max_length=40)
    phone_number = models.Field(max_length=15)
    address = models.TextField(max_length=500)

class Products(models.Model):
    product_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    product_description = models.TextField()
    product_price = models.FloatField()
    product_image = models.ImageField(blank=True, null=True, upload_to='uploads/')
    user_id = models.ForeignKey(User, on_delete= models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete= models.CASCADE) 

class Category(models.Model):
    Category_name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)
    product_id = models.ForeignKey(Products, on_delete= models.CASCADE)
    category_description = models.TextField()
    category_image = models.ImageField(blank=True, null=True, upload_to='uploads/')

class ProductCategory(models.Model):
    category_name = models.ForeignKey(Category, on_delete= models.CASCADE)

class Menu(models.Model):
    product_name = models.ForeignKey(Products, on_delete= models.CASCADE)
    slug = models.SlugField(unique=True)
    product_description =  models.ForeignKey(Products, on_delete= models.CASCADE)
    product_price = models.ForeignKey(Products, on_delete= models.CASCADE)
    product_image =  models.ForeignKey(Products, on_delete= models.CASCADE)
    menu_status

class Orders(models.Model):
    product_id = models.ForeignKey(Products, on_delete= models.CASCADE)
    product_name  = models.ForeignKey(Products, on_delete= models.CASCADE)
    slug = models.SlugField(unique=True)
    product_description =  models.ForeignKey(Products, on_delete= models.CASCADE)
    product_price = models.ForeignKey(Products, on_delete= models.CASCADE)
    product_image =  models.ForeignKey(Products, on_delete= models.CASCADE)
    quantity = models.TextField()
    user_id = models.ForeignKey(User, on_delete= models.CASCADE)
    user_Username = models.ForeignKey(User, on_delete= models.CASCADE)
    user_email = models.ForeignKey(User, on_delete= models.CASCADE)
    user_phonenumber = models.ForeignKey(User, on_delete= models.CASCADE)
    user_address = models.ForeignKey(User, on_delete= models.CASCADE)
    created at datetime NOT NULL
    order_date date NOT NULL 
    total_amount float
    order_status varchar(20)

class Reviews(models.Model):
    user_id = models.ForeignKey(User, on_delete= models.CASCADE)
    menu_id = models.ForeignKey(Menu, on_delete= models.CASCADE)
    score = models.FloatField(1-10)
    remarks = models.TextField()
    date_recorded datetime

class SylviaPhotos(models.Model):
    image1 = models.ImageField(blank=True, null=True, upload_to='uploads/')
    image2 = models.ImageField(blank=True, null=True, upload_to='uploads/')
    image3 = models.ImageField(blank=True, null=True, upload_to='uploads/')
    image4 = models.ImageField(blank=True, null=True, upload_to='uploads/')

class Cart(models.Model):
    product_name  = models.ForeignKey(Products, on_delete= models.CASCADE)
    slug = models.SlugField(unique=True)
    product_description =  models.ForeignKey(Products, on_delete= models.CASCADE)
    product_price = models.ForeignKey(Products, on_delete= models.CASCADE)
    product_image =  models.ForeignKey(Products, on_delete= models.CASCADE)
    quantity = models.TextField()
    user_id = models.ForeignKey(User, on_delete= models.CASCADE)
    user_Username = models.ForeignKey(User, on_delete= models.CASCADE)
    user_email = models.ForeignKey(User, on_delete= models.CASCADE)
    user_phonenumber = models.ForeignKey(User, on_delete= models.CASCADE)

class Blog(models.Model):
    blog_image = models.ImageField(blank=True, null=True, upload_to=/uploads)
    date created
    blog_name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    blog_description = models.TextField()

class HomeSlides(models.Model):
    product_adjective = models.CharField(max_length=20)
    product_name =  models.ForeignKey(Products, on_delete= models.CASCADE)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image1 =  models.ImageField(blank=True, null=True, upload_to=/uploads)

class Team(models.Model):
    image1 =  models.ImageField(blank=True, null=True, upload_to=/uploads)
    team_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    team_description = models.TextField()
    team_bio = models.CharField(max_length=50)

class Payment(models.Model):
    order_id = models.ForeignKey(Order, on_delete= models.CASCADE)
    amount = models.FloatField()
    paid_by = models.CharField(max_length=20)
    payment_date = datetime
    processed_by = models.CharField(max_length=30)

class SiteInfo(models.Model):
    site_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    contact_info = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    last_update = datetime
















