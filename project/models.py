
from django.db import models

# Create your models here.


class Project(models.Model):
    class STATUS_CHOICES(models.TextChoices):
        planned = 'planned', 'Planned',
        in_progress = 'in_progress', 'In Progress',
        completed = 'completed', 'Completed'


    class DIFFICULTY_LEVEL(models.TextChoices):
        easy = 'easy', 'Easy',
        hard = 'hard', 'Hard'
        extreme = 'extreme', 'Extreme',
        kek = 'kek', 'Kek'

    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=20,choices=DIFFICULTY_LEVEL.choices,default=DIFFICULTY_LEVEL.easy)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES.planned)
    start_date = models.DateField()
    assigned_people = models.ManyToManyField(
        to='people.People',
        related_name='projects',
        blank=True)

    def __str__(self):
        return self.title
