from django.urls import path
from books import views

urlpatterns = [
    path('', views.home, name="index"),
    path('books/', views.books, name="books_list"),
]
