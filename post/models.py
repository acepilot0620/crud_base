from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    created = models.DateTimeField(default=timezone.now(), null=True)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
