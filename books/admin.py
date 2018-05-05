from django.contrib import admin
from .models import Author, User, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic')


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'pub_date', 'read_date')
    list_filter = ('pub_date',)
    filter_horizontal = ('authors',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(User)
admin.site.register(Book, BookAdmin)
