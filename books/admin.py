from django.contrib import admin
from .models import Author, User, Book

admin.site.register(Author)
admin.site.register(User)
admin.site.register(Book)
