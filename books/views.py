from books.models import Book
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    latest_books_list = Book.objects.count()
    return render(
        request,
        'index.html',
        context={'num_books': latest_books_list},
    )


def detail(request, book_id):
    return HttpResponse("You're looking at book %s." % book_id)
