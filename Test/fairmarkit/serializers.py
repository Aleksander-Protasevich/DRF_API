from rest_framework_json_api import serializers
from .models import Author, Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'published_year', 'author_id', 'genre', 'rating',)


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('name',)


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('genre',)