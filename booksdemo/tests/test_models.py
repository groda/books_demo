from django.test import TestCase
from ..models import Book, Word


class BookTest(TestCase):
    """ Test module for Book model """

    def setUp(self):
        abstract1 = 'Lorem ipsum dolor sit amet, consectetur adipisici elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquid ex ea commodi consequat. Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        abstract2 = '333 4444 55555 55555 666666'
        Book.objects.create(
           title='Test Title1', author='Test Author1', abstract=abstract1, book_type=2, min_word_size=5)
        Book.objects.create(
           title='Test Title2', author='Test Author2', abstract=abstract2, book_type=2, min_word_size=5)

    def test_book(self):
        book1 = Book.objects.get(title='Test Title1')
        book2 = Book.objects.get(title='Test Title2')
        self.assertEqual(
            book1.get_author(), "Test Author1")
        self.assertEqual(
            book2.get_author(), "Test Author2")


class WordTest(TestCase):
    """ Test module for Word model """

    def setUp(self):
        abstract1 = 'Lorem ipsum dolor sit amet, consectetur adipisici elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquid ex ea commodi consequat. Quis aute iure reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        Book.objects.create(
           title='Test Title1', author='Test Author1', abstract=abstract1, book_type=2, min_word_size=5)

    def test_word(self):
        book1 = Book.objects.get(title='Test Title1')
        Word.objects.create(
           name='Lorem', occurrences=1, book=book1)
        word = Word.objects.get(name='Lorem')
        self.assertEqual(
            word.get_occurrences(), 1)


