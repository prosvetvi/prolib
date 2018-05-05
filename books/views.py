from books.models import Book
from django.http import HttpResponse


def index(request):
    latest_books_list = Book.objects.order_by('-pub_date')[:5]
    output = ', '.join([b.name for b in latest_books_list])
    return HttpResponse(output)


def detail(request, book_id):
    return HttpResponse("You're looking at book %s." % book_id)
