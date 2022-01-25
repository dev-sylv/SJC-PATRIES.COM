from django.contrib import admin
from Snacks_App.models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
# from django.contrib.auth.models import AbstractUser


# Register your models here.
# admin.site.register(User, UserAdmin)

@admin.register(OrderProfile)
class OrderProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('User_name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('Category_name',)}

admin.site.register(ProductCategory)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('snacks_name',)}

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
    def get_blog_image(self, obj):
        return format_html('<img src="{}" width="100"/>'.format(obj.blog_image.url))
    get_blog_image.short_description = 'Blog'

    list_display = [
        'blog_name',
        'get_blog_image',
        'created',
        'user'
    ]

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

admin.site.register(ContactMe)
