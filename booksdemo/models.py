from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class Book(models.Model):
    HARDCOVER = 1
    PAPERBACK = 2
    EBOOK = 3
    HARDCOVER = 1
    PAPERBACK = 2
    EBOOK = 3
    BOOK_TYPES = (
        (HARDCOVER, 'Hardcover'),
        (PAPERBACK, 'Paperback'),
        (EBOOK, 'E-book'),
    )
    title = models.CharField(max_length=140)
    author = models.CharField(max_length=30, blank=True)
    publication_date = models.DateField(null=True)
    pages = models.IntegerField(blank=True, null=True)
    book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES)
    abstract = models.CharField(max_length=2800)


class Word(models.Model):
    name = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    occurrences = models.IntegerField()

    class Meta:
        unique_together = ('name', 'book',)

