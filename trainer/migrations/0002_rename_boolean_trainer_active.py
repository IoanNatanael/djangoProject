# Generated by Django 4.1.6 on 2023-02-15 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainer',
            old_name='boolean',
            new_name='active',
        ),
    ]
