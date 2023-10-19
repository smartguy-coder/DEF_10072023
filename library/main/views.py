from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import logout
from django.shortcuts import redirect

from .models import Book


class BookCreateView(CreateView):
    model = Book
    template_name = 'main/book_edit.html'
    success_url = '/'
    fields = '__all__'


class BookEditView(UpdateView):
    model = Book
    template_name = 'main/book_edit.html'
    success_url = '/'
    fields = '__all__'


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'main/book_delete.html'
    success_url = '/'


class BookListView(ListView):
    queryset = Book.objects.all(
    ).filter(
        # visitor_id__isnull=False,
        # id__lte=100
        # id__gte=6400
        # title__contains='Last'
        # title__exact='Last'
    ).prefetch_related(  # many-to-many
        'author'
    ).select_related(  # one to many
        'visitor'
    )
    template_name = 'main/book_list.html'


def logout_user(request):
    logout(request)
    pass


def books_getter(request):
    # print(request.__dict__, 1111111111111)
    # print(9999999999999)

    books = Book.objects.all(
    ).only(
        'title',
        'price',
    )[:2]
    # print(books.query)
    # print(1111111)

    context = {
        'book_list': books,
        'age': 555555555555
    }

    return render(request, 'main/book_list.html', context=context)
