# Generated by Django 4.1.6 on 2023-02-15 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('department', models.CharField(choices=[('backend', 'Backend'), ('frontend', 'Frontend'), ('network', 'Network')], max_length=10)),
                ('boolean', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
