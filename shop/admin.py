from django.contrib import admin
from .models import Category, Product, Tag

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'sale','available', 'created', 'updated']
    list_filter = ['available', 'sale','created', 'updated', 'tags']
    list_editable = ['price', 'sale','available']
    prepopulated_fields = {'slug': ('name',)}