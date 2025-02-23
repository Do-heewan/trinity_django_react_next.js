from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'publication_date']
    search_fields = ['title', 'author']
    list_filter = ['author', 'publication_date']