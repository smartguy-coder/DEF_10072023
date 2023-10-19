from django.contrib import admin
from django.urls import path, include

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.BookListView.as_view(), name='index'),
    path('book/add/', views.BookCreateView.as_view()),
    path('book/<int:pk>/edit/', views.BookEditView.as_view()),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view()),
    path('func/', views.books_getter),

    path('web/logout/', views.logout_user, name='logout'),


    path("__debug__/", include("debug_toolbar.urls")),
]
