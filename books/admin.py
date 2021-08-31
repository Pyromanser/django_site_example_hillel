from django.contrib import admin
from books.models import Author, Book


class BookInline(admin.TabularInline):
    model = Book
    extra = 2


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name"]
    search_fields = ["first_name", "last_name"]
    inlines = [BookInline]


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ["title", "author"]
    search_fields = ["title", ]
    raw_id_fields = ["author"]

