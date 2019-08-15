from rest_framework import serializers

from .models import Book, Word


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = "__all__"
