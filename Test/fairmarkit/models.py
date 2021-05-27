from django.db import models


class Author (models.Model):
    name = models.CharField('Имя автора', max_length=50)
    
    def __str__(self):
        return self.name
        
class Book (models.Model):
    title = models.CharField(verbose_name = 'Название книги', max_length=40)
    published_year = models.CharField(verbose_name = 'Год издания', max_length=10)
    author_id = models.ForeignKey(Author, on_delete = models.CASCADE, verbose_name ='Автор ID', related_name='books')
    genre = models.CharField(verbose_name = 'Жанр', max_length=40)
    rating = models.PositiveIntegerField(verbose_name = 'Рейтинг (0-10)')

    def __str__(self):
        return self.title