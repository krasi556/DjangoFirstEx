from django.db import models


# Create your models here.


class Qualifications(models.Model):
    date = models.DateField()
    university = models.CharField(max_length=200)
    courses = models.CharField(max_length=200,
                               null=True,
                               blank=True)

