from django.db import models

# Create your models here.

class Sample(models.Model):
    sample_name = models.CharField(max_length=200)
    description = models.TextField(default='')
    time = models.DateTimeField(default='')