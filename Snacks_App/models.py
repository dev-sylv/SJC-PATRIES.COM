from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

# from django.contrib.auth.models import AbstractUser
# from django.conf import settings

class OrderProfile(models.Model):
    First_name = models.CharField(max_length=30)
    First_name = models.CharField(max_length=30)
    User_name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    email = models.EmailField()
    profile_image = models.ImageField(blank=True, null=True, upload_to='uploads/')
    phone_number = models.CharField(max_length=15)
    address = models.TextField(max_length=500)

    def get_profile_image(self):
        if self.profile_image:
            return self.profile_image.url

class Products(models.Model):
    product_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    product_description = models.TextField()
    product_price = models.FloatField()
    product_image = models.ImageField(blank=True, null=True, upload_to='uploads/')
    
    # category_id = models.ForeignKey(Category, on_delete= models.CASCADE) 

    def __str__(self):
        return self.product_name

    class Meta():
        verbose_name_plural = 'Snacks'

    def get_product_image(self):
        if self.product_image:
            return self.product_image.url

class Category(models.Model):
    Category_name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)
    product_id = models.ForeignKey(Products, on_delete= models.CASCADE)
    category_description = models.TextField()
    category_image = models.ImageField(blank=True, null=True, upload_to='uploads/')

    def __str__(self):
        return self.category_name

    def get_category_image(self):
        if self.category_image:
            return self.category_image.url

class ProductCategory(models.Model):
    category_name = models.ForeignKey(Category, on_delete= models.CASCADE)

    class Meta():
        verbose_name_plural = 'ProductCategories'

class Menu(models.Model):
    AVAILABLE = 'available'
    UNAVAILABLE = 'unavailable'
    CHOOSE = ''
    menu_status = [
        (AVAILABLE, 'available'),
        (UNAVAILABLE, 'unavailable'),
        (CHOOSE, 'please choose'),
    ]
    snacks_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    snacks_description =  models.TextField()
    snacks_price = models.CharField(max_length=12)
    snacks_image =  models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name = 'sylvia_image1')
    menu_status = models.CharField(max_length=30, verbose_name= 'Menu Status', choices=menu_status, default = CHOOSE)

    def __str__(self):
        return self.snacks_name

    def get_product_image(self):
        if self.product_image:
            return self.product_image.url

class Orders(models.Model):
    product_id = models.ForeignKey(Products, on_delete= models.CASCADE)
    # product_name  = models.ForeignKey(Products, on_delete= models.CASCADE)
    slug = models.SlugField(unique=True)
    # product_description =  models.ForeignKey(Products, on_delete= models.CASCADE)
    # product_price = models.ForeignKey(Products, on_delete= models.CASCADE)
    # product_image =  models.ForeignKey(Products, on_delete= models.CASCADE)
    quantity = models.TextField()
    user_id = models.ForeignKey(User, on_delete= models.CASCADE)
    # Username = models.ForeignKey(User, on_delete= models.CASCADE)
    # email = models.ForeignKey(User, on_delete= models.CASCADE)
    # phonenumber = models.ForeignKey(User, on_delete= models.CASCADE)
    # address = models.ForeignKey(User, on_delete= models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.FloatField()
    # order_status varchar(20)

    def __str__(self):
        return self.product_name

    def get_product_image(self):
        if self.product_image:
            return self.product_image.url

    class Meta():
        verbose_name_plural = 'Order'

class Reviews(models.Model):
    user_id = models.ForeignKey(User, on_delete= models.CASCADE)
    menu_id = models.ForeignKey(Menu, on_delete= models.CASCADE)
    score = models.FloatField(1-10)
    remarks = models.TextField()
    date_recorded = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name_plural = 'Reviews'

class SylviaPhotos(models.Model):
    image1 = models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name = 'sylvia_image1')
    image2 = models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name = 'sylvia_image2')
    image3 = models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name = 'sylvia_image3')
    image4 = models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name = 'sylvia_image4')

    def get_image1(self):
        if self.image1:
            return self.image1.url

    def get_image2(self):
        if self.image2:
            return self.image2.url

    def get_image3(self):
        if self.image3:
            return self.image3.url   
            
    def get_image4(self):
        if self.image4:
            return self.product_image4.url

    class Meta():
        verbose_name_plural = 'Sylvia-Photos'

class Cart(models.Model):
#     product_name  = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
#     product_description =  models.TextField('Yummy')
#     product_price = models.CharField(max_length=15)
#     product_image =  models.ImageField(blank=True, null=True, upload_to='uploads/')
    quantity = models.TextField()
    user_id = models.ForeignKey(User, on_delete= models.CASCADE)
    # order_Username = models.ForeignKey(OrderProfile, on_delete= models.CASCADE)
    # order_email = models.ForeignKey(OrderProfile, on_delete= models.CASCADE)
    # order_phonenumber = models.ForeignKey(OrderProfile, on_delete= models.CASCADE)

    def __str__(self):
        return self.product_name

    def get_product_image(self):
        if self.product_image:
            return self.product_image.url

class Blog(models.Model):
    FEATURE = 'Feature'
    No_FEATURE ='No Feature'
    CHOOSE = ''
    APPEAR_HOME_FIELD=[
        (FEATURE, 'Appear on home'),
        (No_FEATURE, "Don't show on home"),
        (CHOOSE, 'Please choose'),
    ]
    blog_image = models.ImageField(blank=True, null=True, upload_to='uploads/')
    created = models.DateTimeField(auto_now_add=True)
    appear_home = models.CharField(max_length=50, choices=APPEAR_HOME_FIELD, default=CHOOSE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    blog_description = models.TextField()
    

    class Meta():
        verbose_name_plural = 'Blog'

    def get_blog_image(self):
        if self.blog_image:
            return self.blog_image.url

    def get_absolute_url(self):
        return reverse('Snacks_App:Blog_single', kwargs={
            'slug': self.slug,
        })

    def __str__(self):
        return self.blog_name

class HomeSlides(models.Model):
    product_adjective = models.CharField(max_length=20)
    product_name =  models.ForeignKey(Products, on_delete= models.CASCADE)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    imageA =  models.ImageField(blank=True, null=True, upload_to='uploads/')

    def __str__(self):
        return self.product_name

    def get_imageA(self):
        if self.imageA:
            return self.imageA.url

    class Meta():
        verbose_name_plural: 'HomeSlides'

class Team(models.Model):
    image1 =  models.ImageField(blank=True, null=True, upload_to='uploads/')
    team_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    team_description = models.TextField()
    team_bio = models.CharField(max_length=50)

    def __str__(self):
        return self.team_name

class Payment(models.Model):
    order_id = models.ForeignKey(Orders, on_delete= models.CASCADE)
    amount = models.FloatField()
    paid_by = models.CharField(max_length=20)
    payment_date = models.DateTimeField(auto_now_add=True)
    processed_by = models.CharField(max_length=30)

class SiteInfo(models.Model):
    site_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    contact_info = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.site_name


