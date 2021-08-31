from django.shortcuts import render, get_object_or_404, redirect

from books.models import Book
from books.forms import BookModelForm


def home(request):
    return render(request, "books/home.html")


def books(request):
    return render(request, "books/books_list.html", context={"books": Book.objects.all()})


def book(request, pk):
    return render(request, "books/books_detail.html", context={"book": get_object_or_404(Book, pk=pk)})


def create_book(request):
    if request.method == "GET":
        form = BookModelForm()
    else:
        form = BookModelForm(request.POST)
        if form.is_valid():
            new_book = form.save()
            return redirect("books_detail", pk=new_book.pk)
    return render(request, "books/books_create.html", context={"form": form})


def update_book(request, pk):
    b = get_object_or_404(Book, pk=pk)
    if request.method == "GET":
        form = BookModelForm(instance=b)
    else:
        form = BookModelForm(request.POST, instance=b)
        if form.is_valid():
            new_book = form.save()
            return redirect("books_detail", pk=new_book.pk)
    return render(request, "books/books_update.html", context={"form": form})
