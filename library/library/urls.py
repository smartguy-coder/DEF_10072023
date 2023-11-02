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

    path('logout/', views.logout_user, name='logout'),
    path('registration/', views.RegisterUser.as_view(), name='registration'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('delete_user/<int:pk>', views.DeleteUser.as_view(), name='delete_user'),

    path('api/v1/data/', views.json_data),
    path('api/v1/data_drf/', views.json_data),


    path("__debug__/", include("debug_toolbar.urls")),
]
