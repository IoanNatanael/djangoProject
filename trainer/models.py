from django.db import models

# Create your models here.


class Trainer(models.Model):
    department_options = (('backend', 'Backend'), ('frontend', 'Frontend'), ('network', 'Network'))

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    course = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    department = models.CharField(max_length=10, choices=department_options)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='img/', null=True)
    file = models.FileField(upload_to='file/', null=True)

    hours = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    total = models.IntegerField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'