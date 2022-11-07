from unicodedata import name
from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()

    def __str__(self) -> str:
        return self.name