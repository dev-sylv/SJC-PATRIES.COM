from django.contrib import admin
from Snacks_App.models import *

# Register your models here.
@admin.register(User)
class UserAdmin(model.ModelAdmin):
    prepopulated_fields = {'slug': ('Username',)}

@admin.register(Products)
class ProductsAdmin(model.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}

@admin.register(Category)
class CategoryAdmin(model.ModelAdmin):
    prepopulated_fields = {'slug': ('Category_name',)}

@admin.site.register(ProductCategory)

@admin.register(Menu)
class MenuAdmin(model.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}

@admin.register(Orders)
class OrdersAdmin(model.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}

@admin.site.register(Reviews)

@admin.site.register(SylviaPhotos)

@admin.register(Cart)
class CartAdmin(model.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}

@admin.register(Blog)
class BlogAdmin(model.ModelAdmin):
    prepopulated_fields = {'slug': ('blog_name',)}

@admin.register(HomeSlides)
class HomeSlidesAdmin(model.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}

@admin.register(Team)
class TeamAdmin(model.ModelAdmin):
    prepopulated_fields = {'slug': ('team_name',)}

@admin.site.register(Payment)

@admin.register(SiteInfo)
class SiteInfoAdmin(model.ModelAdmin):
    prepopulated_fields = {'slug': ('site_name',)}


