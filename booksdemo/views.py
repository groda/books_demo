from django.shortcuts import render
from django.http import HttpResponse
import requests
import os
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Greeting
from .models import Book

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


class BookList(ListView):
    model = Book

class BookView(DetailView):
    model = Book

class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author']
    success_url = reverse_lazy('book_list')

class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'author']
    success_url = reverse_lazy('book_list')

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')
