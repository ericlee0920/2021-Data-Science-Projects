from django.db import models
from django.utils import timezone

# Create your models here.

class Sample(models.Model):
    sample_name = models.CharField(max_length=200)
    description = models.TextField()
    time = models.DateTimeField(default=timezone.now)  

    def __str__(self):
        return self.sample_name