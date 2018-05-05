from django.db import models
from django.contrib.auth.models import AbstractUser


class Author(models.Model):
    surname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    patronymic = models.CharField(max_length=200)
    birth_date = models.DateTimeField('date birthday')

    def __str__(self):
        return u'%s %s' % (self.name, self.surname)


class Book(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    read_date = models.DateTimeField('date reading')
    authors = models.ManyToManyField(Author)
    image = models.ImageField(blank=True, null=True)
    file = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    location = models.CharField(max_length=30, blank=True)


class Reading(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_joined = models.DateField()
