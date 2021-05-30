
from django.db import models
from django.utils import timezone

# Create your models here.
class Work(models.Model):
    tasks = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    important = models.BooleanField(default=False)
    due = models.DateTimeField(blank=True)