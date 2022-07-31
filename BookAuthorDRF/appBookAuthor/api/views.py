from rest_framework import viewsets
from appBookAuthor.models import BookType, Authors, Books
from .serializations import BookTypeSerializers, AuthorsSerializers, BooksSerializers

# ViewSets define the view behavior.
class BookTypeViewSet(viewsets.ModelViewSet):
    queryset = BookType.objects.all()
    serializer_class = BookTypeSerializers
    
class AuthorsViewSet(viewsets.ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializers
    
class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializers
    
    def create(self, request, *args, **kwargs):
        print("=================== create ===================")
        print(self.action)
        print(dir(request.data))
        print(request.data)
        print(request.data['title'])
        print("=================== create ===================")
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)