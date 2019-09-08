import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Book, Word
from ..serializers import BookSerializer, WordSerializer


# initialize the APIClient app
client = Client()
