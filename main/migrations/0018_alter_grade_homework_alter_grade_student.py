# Generated by Django 4.0.2 on 2022-03-13 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_grade_datentime_teacher_dareje_teacher_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='homework',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.homework', verbose_name='Үй жұмысы'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.student', verbose_name='Студент'),
        ),
    ]