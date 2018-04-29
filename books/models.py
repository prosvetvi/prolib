from django.db import models


class Author(models.Model):
    surname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    patronymic = models.CharField(max_length=200)
    birth_date = models.DateTimeField('date birthday')


class Book(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    read_date = models.DateTimeField('date published')
    authors = models.ManyToManyField(Author)
