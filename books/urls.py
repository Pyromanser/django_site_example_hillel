from django.urls import path
from books import views

urlpatterns = [
    path('', views.home, name="index"),
    path('books/', views.books, name="books_list"),
    path('books/<int:pk>', views.book, name="books_detail"),
    path('books/create', views.create_book, name="create_book"),
    path('books/update/<int:pk>', views.update_book, name="update_book"),
]
