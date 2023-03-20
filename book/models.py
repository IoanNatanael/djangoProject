from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
