# Generated by Django 4.0.2 on 2022-03-09 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='courses',
        ),
    ]
