from django.shortcuts import render

from books.models import Book


def home(request):
    return render(request, "books/home.html")


def books(request):
    return render(request, "books/books_list.html", context={"books": Book.objects.all()})
