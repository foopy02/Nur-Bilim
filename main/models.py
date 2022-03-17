from distutils.command.upload import upload
from email.policy import default
from io import open_code
from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from sqlalchemy import ForeignKey, null
import uuid

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, role, name, surname, patronymic, password=None):
        if not email:
            raise ValueError("Электронді адресс міндетті")
        if not role:
            raise ValueError("Рөл таңдау міндетті")
        
        user=self.model(
            email=self.normalize_email(email),
            role=role,
            name=name,
            surname=surname,
            patronymic=patronymic
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, role, name, surname, patronymic=None, password=None):
        user=self.create_user(
            email=email,
            role=role,
            password=password,
            name=name,
            surname=surname,
            patronymic=patronymic
        )
        user.is_admin=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class Course(models.Model):
    id=models.AutoField(unique=True, primary_key=True)
    name=models.CharField(max_length=200, verbose_name="Курстың аты", blank=True, null=True)
    creater_email = models.EmailField(max_length=60, verbose_name="Курстың мұғалім поштасы", blank=True, null=True)
    creater_name = models.CharField(max_length=200, verbose_name="Курстың мұғалім аты", blank=True, null=True)
    creater_surname = models.CharField(max_length=200, verbose_name="Курстың мұғалім фамилиясы", blank=True, null=True)
    def __str__(self):
        return self.name

class MyUser(AbstractBaseUser):
    email=models.EmailField(verbose_name="Электронды пошта", max_length=60, unique=True)
    name=models.CharField(max_length=60, verbose_name="Аты-жөн",default='')
    surname=models.CharField(max_length=60, verbose_name="Фамилия",default='')
    patronymic=models.CharField(max_length=60, verbose_name="Әкесінің аты", null=True, blank=True)
    role = models.CharField(max_length=255, verbose_name="Рөл")
    date_joined = models.DateTimeField(auto_now_add=True,editable=True),
    last_login = models.DateTimeField(auto_now=True, verbose_name="Соңғы логин",editable=True),
    is_admin=models.BooleanField(default=False),
    is_active=models.BooleanField(default=True),
    is_staff=models.BooleanField(default=False),
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['role','name','surname']

    objects=MyUserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Student(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    course_level = models.IntegerField(verbose_name="Курс", default=1)
    group_name = models.CharField(max_length=255, verbose_name="Топ", null=True, blank=True, default='' )
    courses = models.ManyToManyField(Course, null=True, blank=True,)

    def __str__(self):
        return self.email

class Teacher(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, null=True, blank=True)
    dareje=models.CharField(max_length=255, verbose_name="Дәреже",  default='Оқытушы')
    phone_number=models.IntegerField(verbose_name="Телефон",null=True, blank=True  )
    def __str__(self):
        return self.user.email
    

class Homework(models.Model):
    id=models.AutoField(unique=True, primary_key=True)
    name=models.CharField(max_length=255, verbose_name="Үй жұмыс аты",  default='Үй жұмысы')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    week_number = models.IntegerField(blank=True, null=True, verbose_name="Апта күні")
    upload_file = models.FileField(blank=True, null=True, verbose_name="Файл", upload_to="homeworks")

class Grade(models.Model):
    id=models.AutoField(unique=True, primary_key=True)
    student=models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Студент",blank=True, null=True )
    homework=models.ForeignKey(Homework, on_delete=models.CASCADE, verbose_name="Үй жұмысы",blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True, verbose_name="Баға")
    datentime = models.DateTimeField(auto_now_add=True, editable=True,blank=True, null=True)
    upload_file = models.FileField(blank=True, null=True, verbose_name="Файл", upload_to="grades")

class Lecture(models.Model):
    id=models.AutoField(unique=True, primary_key=True)
    name=models.CharField(max_length=255, verbose_name="Лекцияның аты", default='Лекция')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    week_number = models.IntegerField(blank=True, null=True, verbose_name="Апта күні")
    upload_file = models.FileField(blank=True, null=True, verbose_name="Файл", upload_to="lectures")

class Practice(models.Model):
    id=models.AutoField(unique=True, primary_key=True)
    name=models.CharField(max_length=255, verbose_name="Практиканың аты", default='Практика')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    week_number = models.IntegerField(blank=True, null=True, verbose_name="Апта күні")
    upload_file = models.FileField(blank=True, null=True, verbose_name="Файл", upload_to="practices")