from django.urls import path
from .views import BooksViewSet

urlpatterns = [
    path('books', BooksViewSet.as_view(), name='books'),
    # path('book_type/', BookTypeViewSet.as_view(),name='book_type'),
]