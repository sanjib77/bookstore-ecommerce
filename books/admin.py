# books/admin.py

from django.contrib import admin
from .models import Category, Book, Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn', 'price', 'stock_quantity', 'is_available']
    list_filter = ['category', 'is_available', 'created_at']
    search_fields = ['title', 'author', 'isbn']
    list_editable = ['price', 'stock_quantity', 'is_available']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']