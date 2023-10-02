from decimal import Decimal

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50, null=False)
    price = models.DecimalField(max_length=8, decimal_places=2, default=Decimal('1.00'),
                                )
