# Generated by Django 4.0.2 on 2022-03-13 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_student_course_level_student_group_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='phone',
            new_name='phone_number',
        ),
        migrations.AlterField(
            model_name='student',
            name='group_name',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Топ'),
        ),
    ]
