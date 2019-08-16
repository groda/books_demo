from rest_framework import serializers
from collections import Counter

from .models import Book, Word


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    words = WordSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = "__all__"

    def create(self, validated_data):
        book = Book.objects.create(**validated_data)
        txt = validated_data.pop('abstract')
        min_len = validated_data.pop('min_word_size')
        Word.objects.filter(book=book).delete()
        # tokenize abstract
        for k,v in Counter(txt.split(' ')).items():
            if len(k)>=min_len:
                word = Word.objects.create(name=k, occurrences=v, book=book)
                word.save()
        return book

