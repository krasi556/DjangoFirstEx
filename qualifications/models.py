import uuid

from django.db import models
from django.utils.text import slugify


# Create your models here.


class Qualifications(models.Model):
    date = models.DateField()
    university = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True, unique=True)
    courses = models.CharField(max_length=200,
                               null=True,
                               blank=True)

    def __str__(self):
        return self.university

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f'{slugify(self.university)}-{str(uuid.uuid4())[:3]}'

        super().save(*args, **kwargs)
