from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    first_name = models.CharField(_("first name"), max_length=100)
    last_name = models.CharField(_("last name"), max_length=100)

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")
        unique_together = [["first_name", "last_name"], ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(_("title"), max_length=255, unique=True)
    description = models.TextField(_("description"))
    author = models.ForeignKey("books.Author", verbose_name=_("author"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

    def __str__(self):
        return self.title
