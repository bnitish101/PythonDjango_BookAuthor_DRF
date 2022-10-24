from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView 
from .models import Books, Authors, BookType
from django.db.models import Q
# Create your views here.

class BooksViewSet(ListView):
    model = Books
    context_object_name = 'books'
    # template_name = 'appBookAuthor/author.html'
    con1 = Books.objects.filter(pk=1)
    q1 = con1.query
    con2 = con1.distinct()
    q2 = con2.query
    con3 = con1.distinct().select_related()
    q3 = con3.query
    
    con4 = BookType.objects.filter(Q(Q(books__title__isnull=False) | Q(books__title__isnull=True)) & Q(books__title="Book1")) \
        .values('books__price') 
    q4 = con4.query
    
    # con5 = con4.prefetch_related() 
    con5 = BookType.objects.prefetch_related('books_set').filter(books__title__iexact="Mystery").values('books__title')  
    q5 = con5.query
    
    extra_context = {"k1": q1, "k2": q2, "k3": q3, "k4": q4, "k5": q5}
    # extra_context = "k1"
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     # context['my_context'] = {"k1": "v1", "k2": "v2"}
    #     context['my_context'] = "k"
    #     context['my_context1'] = "k1"
    #     context['my_context2'] = "k2"
    #     context['my_context3'] = "k3"
    #     return context