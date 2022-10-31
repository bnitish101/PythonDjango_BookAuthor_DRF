from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView 
from .models import Books, Authors, BookType
from django.db.models import Q, F, Count, OuterRef
# from django.contrib.postgres.aggregates import StringAgg
# Create your views here.

class BooksViewSet(ListView):
    model = Books
    context_object_name = 'books'
    queryset = Books.objects.select_related()
    print(queryset.query)

class BooksViewSetQueryPrint(ListView):
    model = Books
    context_object_name = 'books'
    template_name = 'appBookAuthor/books_query.html'
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

    con6 = BookType.objects.get(Q(pk=2))
    q6 = con6.books_set.filter().exclude(id=1).exclude(id=2)
    q6 = q6.query

    # bt = BookType.objects.
    con7 = BookType.objects.prefetch_related('books_set').filter(books__id = 2)
    q7 = con7
    q7 = vars(q7[0].books_set.all()[0])

    # retrieve the all the records from many to many relationship using for loop 
    books = Books.objects.select_related()
    result =[]
    for book in books:
        _auths_name = []
        for auth in book.author.all():
            _auths_name.append({"auth_name": auth.name, "auth_city": auth.city, "auth_dob": auth.dob})
        result.append({
            'book_name': book.title,
            'book_type': {"bt_name": book.book_type.name, "bt_created_at": book.book_type.created_at},
            'author_name': _auths_name
        })
    
    # OUTPUT
    '''
    result = 
    [
        {
            'book_name': 'Book1',
            'book_type': {
            'bt_name': 'Sci-Fi',
            'bt_created_at': 'datetime.datetime(2022,7,31,13,22,3,717378,tzinfo=datetime.timezone.utc)'
            },
            'author_name': [
            {
                'auth_name': 'Author2',
                'auth_city': 'Mumbai',
                'auth_dob': 'datetime.date(2022,6,1)'
            },
            {
                'auth_name': 'Author3',
                'auth_city': 'Goa',
                'auth_dob': 'datetime.date(2022,4,1)'
            }
            ]
        },
        {
            'book_name': 'Book2',
            'book_type': {
            'bt_name': 'Thriller',
            'bt_created_at': 'datetime.datetime(2022,7,31,13,22,21,360901,tzinfo=datetime.timezone.utc)'
            },
            'author_name': [
            {
                'auth_name': 'Author1',
                'auth_city': 'Mumbai',
                'auth_dob': 'datetime.date(2022,6,1)'
            },
            {
                'auth_name': 'Author2',
                'auth_city': 'Mumbai',
                'auth_dob': 'datetime.date(2022,6,1)'
            },
            {
                'auth_name': 'Author3',
                'auth_city': 'Goa',
                'auth_dob': 'datetime.date(2022,4,1)'
            }
            ]
        },
        {
            'book_name': 'Book3',
            'book_type': {
            'bt_name': 'Mystery',
            'bt_created_at': 'datetime.datetime(2022,7,31,13,22,12,774725,tzinfo=datetime.timezone.utc)'
            },
            'author_name': [
            {
                'auth_name': 'Author4',
                'auth_city': 'Delhi',
                'auth_dob': 'datetime.date(2000,1,1)'
            }
            ]
        },
        {
            'book_name': 'Book4',
            'book_type': {
            'bt_name': 'Fantasy',
            'bt_created_at': 'datetime.datetime(2022,7,31,13,21,54,484780,tzinfo=datetime.timezone.utc)'
            },
            'author_name': [
            {
                'auth_name': 'Author4',
                'auth_city': 'Delhi',
                'auth_dob': 'datetime.date(2000,1,1)'
            }
            ]
        },
        {
            'book_name': 'Book5',
            'book_type': {
            'bt_name': 'Thriller',
            'bt_created_at': 'datetime.datetime(2022,7,31,13,22,21,360901,tzinfo=datetime.timezone.utc)'
            },
            'author_name': [
            {
                'auth_name': 'Author1',
                'auth_city': 'Mumbai',
                'auth_dob': 'datetime.date(2022,6,1)'
            },
            {
                'auth_name': 'Author3',
                'auth_city': 'Goa',
                'auth_dob': 'datetime.date(2022,4,1)'
            },
            {
                'auth_name': 'Author4',
                'auth_city': 'Delhi',
                'auth_dob': 'datetime.date(2000,1,1)'
            }
            ]
        }
    ]
    '''
    ex_books = Books.objects.select_related().annotate(
    my_id=F('id'), 
    # auths=F(
    #     Books.objects.filter(id=F('id')).author.all()
    #     )
    )
    # ex_books = ex_books.book.author.all()
    # ex_books =Books.objects.annotate(
    #     _annotated_value=F(dir('id'))
    #     )
    
    # for PostgreSQL 
    # https://code.djangoproject.com/ticket/31097
    
    # for SQL 
    # https://stackoverflow.com/questions/10340684/group-concat-equivalent-in-django

    print("-----------s ex_books -----------")
    print(ex_books.query)
    print("-----------e ex_books -----------")

    extra_context = {"k1": q1, "k2": q2, "k3": q3, "k4": q4, "k5": q5, "k6": q6, "k7": q7, "v7": vars(con7[0]), "v8": result}
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