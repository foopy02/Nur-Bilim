# Generated by Django 4.0.2 on 2022-03-09 12:47

from django.db import migrations, models
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_myuser_email_alter_myuser_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Курстың аты')),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='courses',
            field=models.ManyToManyField(default=sqlalchemy.sql.expression.null, to='main.Course'),
        ),
    ]
