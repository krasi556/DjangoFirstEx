from django.db import models

from people.models import People


# Create your models here.

class Address(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    person = models.ForeignKey(
        to=People,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='addresses'
    )

