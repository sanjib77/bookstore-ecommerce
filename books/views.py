# books/views.py

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q, Avg
from .models import Book, Category, Review

class BookListView(ListView):
    """Display list of all books"""
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = Book.objects.filter(is_available=True)
        
        # Search functionality
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(author__icontains=search_query) |
                Q(isbn__icontains=search_query)
            )
        
        # Category filter
        category_slug = self.request.GET.get('category')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class BookDetailView(DetailView):
    """Display single book details"""
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        context['reviews'] = book.reviews.all()
        context['average_rating'] = book.reviews.aggregate(Avg('rating'))['rating__avg']
        return context


def home(request):
    """Homepage"""
    featured_books = Book.objects.filter(is_available=True)[:8]
    categories = Category.objects.all()[:6]
    
    context = {
        'featured_books': featured_books,
        'categories': categories,
    }
    return render(request, 'home.html', context)