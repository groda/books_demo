from django.shortcuts import render
from django.http import HttpResponse
import requests
import os
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book, Word
from rest_framework import generics, viewsets
from .serializers import BookSerializer, WordSerializer
from rest_framework.response import Response
from collections import Counter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
def index(request):
    name = os.environ.get('UNAME')
    return HttpResponse('Books demo app')

def books(request):
###    if request.method == 'POST':
###        # tokenize abstract
###        txt = request.POST.get('abstract').split(' ')
###        id = request.POST.get('id')
###        for k,v in Counter(txt.split(' ')).items(): 
###            word = Word(name=k, occurrences=v, book=id)
###            word.save()
    books = Book.objects.all()
    context = {
        'books': books
    } 
    return render(request('listing_books.html', context))

def words(request):
    words = Word.objects.all()
    context = {
        'words': words
    } 
    return render(request('listing_words.html', context))

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author']

class WordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['book', 'occurrences']
