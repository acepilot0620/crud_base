from django.db import models
from django.utils import timezone
from account.models import Account

# Create your models here.

class Post(models.Model):
    created = models.DateTimeField(default=timezone.now(), null=True)
    writer = models.ForeignKey(Account,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
