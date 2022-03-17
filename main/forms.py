from attr import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Course, Grade, Homework, Lecture, MyUser, Practice
from django.contrib.auth import authenticate

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=MyUser
        fields=('email','role','name','surname','password1','password2')


class AuthUserForm(forms.ModelForm):
    password=forms.CharField(label="password", widget=forms.PasswordInput )
    class Meta:
        model = MyUser
        fields = ['email', 'password']
    
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password=self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid credentials")


class CourseCreationForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=['name', 'creater_email']


class HomeWorkCreationForm(forms.ModelForm):
    class Meta:
        model=Homework
        fields = "__all__"

class GradeCreationForm(forms.ModelForm):
    class Meta:
        model=Grade
        fields = "__all__"

class LectureCreationForm(forms.ModelForm):
    class Meta:
        model=Lecture
        fields = "__all__"

class PracticeCreationForm(forms.ModelForm):
    class Meta:
        model=Practice
        fields = "__all__"
    
