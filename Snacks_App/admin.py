from django.contrib import admin
from Snacks_App.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import AbstractUser


# Register your models here.
admin.site.register(User, UserAdmin)

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('Category_name',)}

admin.site.register(ProductCategory)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('menu_status',)}

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('quantity',)}

admin.site.register(Reviews)

admin.site.register(SylviaPhotos)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('quantity',)}

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('blog_name',)}

@admin.register(HomeSlides)
class HomeSlidesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('team_name',)}

admin.site.register(Payment)

@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('site_name',)}


