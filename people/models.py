from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify

from qualifications.models import Qualifications


# Create your models here.


class People(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(
        validators=[
            MinValueValidator(18, message='You must be over 18')
        ]
    )
    job_description = models.CharField(max_length=200)
    qualifications = models.ManyToManyField(
        to=Qualifications,
        blank=True,
        related_name='people'
    )


    def __str__(self):
        return self.name


