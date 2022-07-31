from rest_framework import serializers
from appBookAuthor.models import BookType, Books, Authors

class BookTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookType
        fields = '__all__'

class AuthorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'

class BooksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
        depth = 1

