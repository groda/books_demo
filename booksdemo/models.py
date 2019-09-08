from django.db import models

class Book(models.Model):
    HARDCOVER = 1
    PAPERBACK = 2
    EBOOK = 3
    BOOK_TYPES = (
        (HARDCOVER, 'Hardcover'),
        (PAPERBACK, 'Paperback'),
        (EBOOK, 'E-book'),
    )
    title = models.CharField(max_length=140)
    author = models.CharField(max_length=100)
    publication_date = models.DateField(null=True)
    pages = models.IntegerField(blank=True, null=True)
    book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES)
    abstract = models.CharField(max_length=28000)
    min_word_size = models.IntegerField(default=3)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_author(self):
        return self.author

    def __str__(self):
        return '{} by {}'.format(self.title, self.author)
    class Meta:
        unique_together = ('title', 'author',)
    
    # https://docs.djangoproject.com/en/2.2/topics/db/models/#overriding-predefined-model-methods
    def save(self, *args, **kwargs):
        #do_something()
        super().save(*args, **kwargs)  # Call the "real" save() method.

class Word(models.Model):
    name = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    occurrences = models.IntegerField()

    def get_occurrences(self):
        return self.occurrences

    class Meta:
        unique_together = ('name', 'book',)

