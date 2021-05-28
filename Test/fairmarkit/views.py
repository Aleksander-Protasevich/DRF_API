from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer,  GenreSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Count, Max
from rest_framework.decorators import action
# from django_filters import rest_framework as filters
from rest_framework import status
from django.shortcuts import get_object_or_404
from random import randint


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def list(self, request, *args, **kwargs):
        for_header = str(randint(0,9))
        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset,
                       context={'request':request},
                       many=True)
        return Response(serializer.data, headers={'X-Test-Header': for_header})

    def retrieve(self, request, pk=None):
        for_header = str(randint(0,9))
        queryset = Author.objects.all()
        author = get_object_or_404(queryset, pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, headers={'X-Test-Header': for_header})
    
    @action(detail=False, methods=['get'])
    def top(self, request):
        for_header = str(randint(0,9))
        queryset = Author.objects.annotate(num_books=Count('books')).order_by('-num_books')[:10]
        serializer = AuthorSerializer(queryset,
                       context={'request':request},
                       many=True)
        return Response(serializer.data, headers={'X-Test-Header': for_header})
    
    def destroy(self, request, pk):
        for_header = str(randint(0,9))
        queryset = Author.objects.all()
        author = get_object_or_404(queryset, pk=pk)
        author.is_active = False
        author.save()
        return Response(status=status.HTTP_204_NO_CONTENT, headers={'X-Test-Header': for_header})


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        for_header = str(randint(0,9))
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset,
                       context={'request':request},
                       many=True)
        return Response(serializer.data, headers={'X-Test-Header': for_header})

    def retrieve(self, request, pk=None):
        for_header = str(randint(0,9))
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(book,context={'request':request})
        return Response(serializer.data, headers={'X-Test-Header': for_header})

    @action(detail=False, methods=['get'])
    def top(self, request):
        for_header = str(randint(0,9))
        queryset = Book.objects.annotate(max_rating=Max('rating')).order_by('-max_rating')[:10]
        serializer = BookSerializer(queryset,
                       context={'request':request},
                       many=True)
        return Response(serializer.data, headers={'X-Test-Header': for_header})
    
    def destroy(self, request, pk):
        for_header = str(randint(0,9))
        queryset = Book.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        book.is_active = False
        book.save()
        return Response(status=status.HTTP_204_NO_CONTENT, headers={'X-Test-Header': for_header})


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = GenreSerializer

    def list(self, request, *args, **kwargs):
        for_header = str(randint(0,9))
        queryset = Book.objects.all()
        serializer = GenreSerializer(queryset,
                       context={'request':request},
                       many=True)
        return Response(serializer.data, headers={'X-Test-Header': for_header})

