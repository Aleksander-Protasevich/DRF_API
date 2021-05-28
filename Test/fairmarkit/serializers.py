from rest_framework_json_api import serializers
from .models import Author, Book
from django.db.models import Count


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'published_year', 'author_id', 'genre', 'rating',)


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('name',)

class GenreSerializer(serializers.ModelSerializer):
    books_in_genre = serializers.SerializerMethodField('book_genre')

    def book_genre(self, obj):
        set = list(Book.objects.values("genre").annotate(num_books= Count("genre")).order_by())
        return set

    class Meta:
        model = Book
        fields = ('books_in_genre',)