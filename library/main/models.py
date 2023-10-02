from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50, null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal('1.00'),
                                validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_created=True, auto_now=True)
    last_change_at = models.DateTimeField(auto_now_add=True)
    pages = models.IntegerField()
    author = models.ManyToManyField('Author', blank=False)

    def __str__(self):
        return f'{self.title} - {self.pages}'

    def __len__(self):
        return self.pages


class Author(models.Model):
    name = models.CharField(max_length=100, blank=False)
    pseudonym = models.CharField(max_length=100, default='')
    has_bad_mude = models.BooleanField(default=False)


class AuthorDetails(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    biography = models.TextField()
