# Generated by Django 4.0.2 on 2022-03-11 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_course_id_alter_homework_id_alter_lecture_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='student',
        ),
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, null=True, to='main.Course'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='courses',
            field=models.ManyToManyField(blank=True, null=True, to='main.Course'),
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('grade', models.IntegerField(blank=True, null=True, verbose_name='Баға')),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='', verbose_name='Файл')),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.homework', verbose_name='Студент')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student', verbose_name='Студент')),
            ],
        ),
    ]