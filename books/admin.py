from django.contrib import admin
from .models import Author, User, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic')


admin.site.register(Author, AuthorAdmin)
admin.site.register(User)
admin.site.register(Book)
