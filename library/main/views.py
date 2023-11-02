from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import logout, login
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from rest_framework.response import Response

from .forms import LoginUserForm, RegisterUserForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework import generics, status
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer
from .tasks import raise_price


class BookAPIView(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        new_book = Book.objects.create(
            title=request.data['title'],
            price=request.data['price'],
            pages=request.data['pages']
        )
        return Response({'new_book': model_to_dict(new_book)}, status=status.HTTP_201_CREATED)


class BookListAPIView(generics.ListAPIView):
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
    serializer_class = BookSerializer


def json_data(request):
    book = Book.objects.all().first()
    result = {
        'title': book.title,
        # 'author': book.author,
        'price': book.price
    }

    return JsonResponse(result)


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Book.objects.all()[:3]
        return context


def logout_user(request):
    logout(request)
    return redirect('index')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

class DeleteUser(PermissionRequiredMixin, DeleteView):
    model = User
    template_name = 'main/delete_user.html'

    def get_success_url(self):
        return reverse_lazy('index')

    def handle_no_permission(self):
        return reverse_lazy('index')


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
    paginate_by = 5000

def books_getter(request):
    # print(request.__dict__, 1111111111111)
    # print(9999999999999)

    books = Book.objects.all(
    ).only(
        'title',
        'price',
    )
    print(books.query, 22222222222)

    context = {
        'book_list': books,
        'age': 555555555555
    }

    raise_price.delay()

    return render(request, 'main/book_list.html', context=context)
