# Generated by Django 4.0.2 on 2022-03-13 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_homework_name_lecture_name_practice_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='datentime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='dareje',
            field=models.CharField(default='Оқытушы', max_length=255, verbose_name='Дәреже'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='course',
            name='creater_email',
            field=models.EmailField(blank=True, max_length=60, null=True, verbose_name='Курстың мұғалім поштасы'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='upload_file',
            field=models.FileField(blank=True, null=True, upload_to='grades', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='upload_file',
            field=models.FileField(blank=True, null=True, upload_to='lectures', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='practice',
            name='upload_file',
            field=models.FileField(blank=True, null=True, upload_to='practices', verbose_name='Файл'),
        ),
    ]