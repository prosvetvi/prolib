from books.models import Book
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    latest_books_list = Book.objects.order_by('-pub_date')[:5]
    output = ', '.join([b.name for b in latest_books_list])
    return render(
        request,
        'index.html',
        context={'num_books': output, 'num_instances': output, 'num_instances_available': output,
                 'num_authors': output, 'num_visits': output},
    )


def detail(request, book_id):
    return HttpResponse("You're looking at book %s." % book_id)
