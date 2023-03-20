from django.db import models

from trainer.models import Trainer


class Student(models.Model):
    gender_options = (('male', 'Male'), ('female', 'Female'))

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(max_length=50)
    description = models.TextField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)
    gender = models.CharField(max_length=6, choices=gender_options)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # auto_not_add=True-> va stoca data si ora in momentul in care voi salva studentul in tabela.
    # NU SE MAI POATE SCHIMBA DATA SI ORA
    # auto_now = True ->va stoca data si ora in momentul salvarii. Data si ora va fi actualizata de
    # fiecare data cand realizez ca modifcari asupra studentului

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
