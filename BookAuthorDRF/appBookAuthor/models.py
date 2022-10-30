from django.db import models

# Create your models here.
class BookType(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'tbl_book_type'

    def __str__(self) -> str:
        return self.name

class Authors(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'tbl_authors'
    
    def __str__(self) -> str:
        return self.name

class Books(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    publish_date = models.DateField()
    price = models.FloatField()
    book_type = models.ForeignKey(BookType, on_delete=models.CASCADE)
    author = models.ManyToManyField(Authors, related_name="book_author")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'tbl_books'
    
    def __str__(self) -> str:
        return self.title
