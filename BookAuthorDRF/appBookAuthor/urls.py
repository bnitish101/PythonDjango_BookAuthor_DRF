from django.urls import path
from .views import BooksViewSet, BooksViewSetQueryPrint

urlpatterns = [
    path('books_query', BooksViewSetQueryPrint.as_view(), name='books_query'),
    path('books', BooksViewSet.as_view(), name='books'),
    # path('book_type/', BookTypeViewSet.as_view(),name='book_type'),
]