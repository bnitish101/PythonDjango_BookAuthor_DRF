from rest_framework import routers, serializers, viewsets
from .views import BookTypeViewSet, AuthorsViewSet, BooksViewSet
from django.urls import path, include
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'book_type', BookTypeViewSet, basename='book_type')
router.register(r'authors', AuthorsViewSet, basename='authors')
router.register(r'books', BooksViewSet, basename='books')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # path('book_type/', BookTypeViewSet.as_view(),name='book_type'),
]