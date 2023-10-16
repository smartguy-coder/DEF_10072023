from django.contrib import admin
from django.urls import path

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.BookListView.as_view()),
    path('book/add/', views.BookCreateView.as_view()),
    path('book/<int:pk>/edit/', views.BookEditView.as_view()),
    path('func/', views.books_getter),
]
