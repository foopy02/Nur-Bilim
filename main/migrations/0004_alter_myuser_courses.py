# Generated by Django 4.0.2 on 2022-03-09 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_course_myuser_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='courses',
            field=models.ManyToManyField(to='main.Course'),
        ),
    ]