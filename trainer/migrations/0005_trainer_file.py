# Generated by Django 4.1.6 on 2023-03-01 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0004_trainer_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='file',
            field=models.FileField(null=True, upload_to='file/'),
        ),
    ]
