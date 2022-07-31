from django.contrib import admin
from .models import BookType, Books, Authors
# Register your models here.

@admin.register(BookType)
class BookTypeAdmin(admin.ModelAdmin):
    list_display = ["name","created_at","updated_at"]


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ["title","description","publish_date","price","book_type","created_at","updated_at"]


@admin.register(Authors)
class AuthorsTypeAdmin(admin.ModelAdmin):
    list_display = ["name","books","city","dob","created_at","updated_at"]