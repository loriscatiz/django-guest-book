from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=255)
    body = models.TextField(null=True)
