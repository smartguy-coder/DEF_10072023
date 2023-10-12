from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Book


class BookListView(ListView):
    queryset = Book.objects.all()
    template_name = 'main/book_list.html'


def books_getter(request):
    books = Book.objects.all(
    ).only(
        'title',
        'price',
    )[:2]
    print(books.query)
    print(1111111)

    context = {
        'book_list': books,
        'age': 555555555555
    }

    return render(request, 'main/book_list.html', context=context)