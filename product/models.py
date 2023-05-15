from django.db import models

# Create your models here.
class Product(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password = models.IntegerField(max_length=20)
    background = models.TextField()
    alive = models.BooleanField(default=True)
