from django.shortcuts import render
from django.http import HttpResponse
import requests
import os
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Greeting
from .models import Book, Word
from rest_framework import generics
from .serializers import BookSerializer, WordSerializer

# Create your views here.
def index(request):
    times = int(os.environ.get('TIMES',3))
    name = os.environ.get('UNAME')
    return HttpResponse('Hello! ' * times + name)


def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, "db.html", {"greetings": greetings})

class BookAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class WordAPIView(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
