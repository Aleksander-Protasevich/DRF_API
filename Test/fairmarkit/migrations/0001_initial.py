# Generated by Django 3.2.3 on 2021-05-23 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя автора')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Название книги')),
                ('published_year', models.CharField(max_length=10, verbose_name='Год издания')),
                ('genre', models.CharField(max_length=40, verbose_name='Название книги')),
                ('rating', models.PositiveIntegerField(verbose_name='Рейтинг (0-10)')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='fairmarkit.author', verbose_name='Автор ID')),
            ],
        ),
    ]
