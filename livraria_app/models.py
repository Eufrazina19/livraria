from django.db import models
from django.urls import reverse
from djmoney.models.fields import MoneyField
from datetime import date


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    # TODO add created by field to track the user who created a particular book
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('publisher-detail', kwargs={'pk': self.pk})


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)
    headshot = models.ImageField(upload_to='livraria_app/static/livraria_app/image/authors',
                                 default='livraria_app/static/livraria_app/image/authors/default_headshot.png')
    biography = models.TextField(blank=True, max_length=5000)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})


class Category(models.Model):
    name = models.CharField(unique=True, max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'pk': self.pk})


class Book(models.Model):
    ISBN = models.BigIntegerField('ISBN')  # TODO find a regex to verify each book isbn.
    cover = models.ImageField('cover photo', upload_to='livraria_app/static/livraria_app/image/books',
                              default='livraria_app/static/livraria_app/image/books/default_book_cover.jpg')
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField('Author')
    categories = models.ManyToManyField('Category')
    pages = models.IntegerField('Number of pages', blank=True)
    # publication_date = models.DateField('Date published', blank=True)
    # edition = models.CharField(max_length=2)
    active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})
