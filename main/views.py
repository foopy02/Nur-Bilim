import re
from tkinter.messagebox import NO
from django.shortcuts import redirect, render
from matplotlib.style import context
from numpy import mat
from .forms import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from .models import Course, Grade, Lecture, Practice, Student, Teacher

# Create your views here.
def get_teachers_courses(request, context):
    courses = Course.objects.filter(creater_email=request.user)
    context['courses'] = courses
    return context

def get_students_courses(request, context):
    student = Student.objects.get(user=request.user)
    courses = student.courses.all()
    context['courses'] = courses
    return context  

def index(request, context={}):

    context['available_courses']= Course.objects.all()
    if request.user.is_authenticated and request.user.role == "teacher":
        context = get_teachers_courses(request, context)
    if request.user.is_authenticated and request.user.role == "student":
        context = get_students_courses(request, context)
    print(context)
    return render(request, 'main/index.html', context)



def register(request):
    context = {

    }
    if request.user.is_authenticated and request.user.role == "teacher":
        context = get_teachers_courses(request, context)
    if request.user.is_authenticated and request.user.role == "student":
        context = get_students_courses(request, context)
    if request.POST:
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = request.POST['role']
            if role == 'teacher':
                Teacher(user=user).save()
            else:
                Student(user=user).save()
            return redirect('login')
        context['register_form']=form

    else:
        form=UserRegistrationForm()
        context['register_form']=form
    return render(request, 'main/register.html', context)

def login_view(request):
    context={}
    if request.user.is_authenticated and request.user.role == "teacher":
        context = get_teachers_courses(request, context)
    if request.user.is_authenticated and request.user.role == "student":
        context = get_students_courses(request, context)
    if request.POST:
        form=AuthUserForm(request.POST)
        context['login_form'] = form
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user = authenticate(request, email=email, password=password)
            print("login")
            if user is not None:
                login(request, user)
                return redirect('index')
        else:
            context['error_log']='Пароль немесе пошта дұрыс емес'
            print("gogo")
            render(request, 'main/login.html', context)
    else:
        form=AuthUserForm()
        context['login_form']=form
    print("hello")
    return render(request, 'main/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('index')

def create_course(request):
    context = {

    }
    if request.user.is_authenticated and request.user.role == "teacher":    
        context = get_teachers_courses(request, context)
    if request.user.is_authenticated and request.user.role == "student":    
        context = get_students_courses(request, context)
    if request.POST:
        form=CourseCreationForm(request.POST)
        if form.is_valid():
            course = form.save()
            course.creater_name = request.user.name
            course.creater_surname = request.user.surname
            course.save()
            
            # course.name = 
            return redirect('index')
        context['creation_form']=form

    else:
        form=CourseCreationForm()
        context['creation_form']=form
    return render(request, 'main/course_create.html', context)

def add_to_course(request):
    context = {

    }
    if request.user.role == "teacher":
        context = get_teachers_courses(request, context)
    if request.user.is_authenticated and request.user.role == "student":
        context = get_students_courses(request, context)
    if request.POST:
        id_of_course = request.POST.get('id')
        emails = request.POST.get('emails').split(',')
        course = Course.objects.get(id=id_of_course)
        for email in emails:
            student = Student.objects.get(user__email = email)
            student.courses.add(course)
            student.save()
        return redirect('index')


def course_page(request, id):

    context = {
        'course': Course.objects.get(id=id)
    }
    materials = []
    for i in range(10):
        i+=1
        lectures = list(Lecture.objects.filter(course=context['course']).filter(week_number=i))
        practices = list(Practice.objects.filter(course=context['course']).filter(week_number=i))
        homeworks = list(Homework.objects.filter(course=context['course']).filter(week_number=i))
        week = {
            'lectures': lectures,
            'practices': practices,
            'homeworks': homeworks
        }
        materials.append(week)
    context['materials'] = materials
    if request.user.role == "teacher":
        context = get_teachers_courses(request, context)
    if request.user.is_authenticated and request.user.role == "student":
        context = get_students_courses(request, context)
    return render(request, 'main/subject.html', context)

def students_of_course(request, id):
    context = {
        'courseid':id,
        'students': Student.objects.filter(courses__id = id),
        'homeworks': Grade.objects.filter(homework__course__id=id)
    }
    if request.user.role == "teacher":
        context = get_teachers_courses(request, context)
    return render(request, 'main/students.html', context)


def create_homeworks(request):
    context = {
    }
    if request.POST:
        form=HomeWorkCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        context['creation_form']=form
    else:
        form=HomeWorkCreationForm()
        context['creation_form']=form

def create_lecture(request):
    context = {
    }
    if request.POST:
        form=LectureCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        context['creation_form']=form
    else:
        form=LectureCreationForm()
        context['creation_form']=form

def create_practice(request):
    context = {
    }
    if request.POST:
        form=PracticeCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        context['creation_form']=form
    else:
        form=PracticeCreationForm()
        context['creation_form']=form

def put_grade(request, id):
    grade = Grade.objects.get(id=id)
    courseid = int(request.POST.get('course_id'))
    given_grade = int(request.POST.get('grade'))
    grade.grade = given_grade
    grade.save()
    return students_of_course(request,courseid)

def create_grade(request):
    if request.POST:
        form=GradeCreationForm(request.POST, request.FILES)
        student = Student.objects.get(user__email=request.user)
        homework_id = request.POST.get('homework_id')
        homework = Homework.objects.get(id=homework_id)
        if form.is_valid():
            grade = form.save()
            grade.student = student
            grade.homework = homework
            grade.grade = 0
            grade.save()
            return redirect('index')
        context['creation_form']=form
    else:
        form=GradeCreationForm()
        context['creation_form']=form

def get_grades(request, email):
    context = {
        'homeworks': Grade.objects.filter(student__user__email=email)
    }
    if request.user.is_authenticated and request.user.role == "student":
        context = get_students_courses(request, context)
    return render(request, 'main/grades.html', context)

def add_student_to_course(request):
    context = {
        
    }
    email = request.POST['email']
    id_of_course = request.POST.get('id')
    course = Course.objects.get(id=id_of_course)
    student = Student.objects.get(user__email = email)
    student.courses.add(course)
    student.save()
    context = {
        'message': "Курска сәтті тіркелдіңіз!"
    }
    return index(request, context)

def student_profile(request, email):
    context = {

    }
    
    return render(request, 'main/profile.html', context)

def teacher_profile(request, email):
    context = {

    }
    return render(request, 'main/profile.html', context)
    
def my_profile(request, context={}):
    context = {
    }
    if request.user.role == "teacher":
        context['profile_user'] = Teacher.objects.get(user__email = request.user)
    else:
        context['profile_user'] = Student.objects.get(user__email = request.user)

    return render(request, 'main/profile.html', context)
    
def save_main_info(request):
    user = MyUser.objects.get(email=request.user)
    user.email = request.POST.get('email')
    user.name = request.POST.get('name')
    user.surname = request.POST.get('surname')
    user.save()
    context = {

    }
    context['message'] = "Сәтті ақпараттар өзгертілді"
    return index(request, context)
 

def save_secondary_info_student(request):
    student = Student.objects.get(user__email=request.user)
    student.course_level = request.POST.get('course_level')
    student.group_name = request.POST.get('group_name')
    student.save()
    context = {

    }
    context['message'] = "Сәтті ақпараттар өзгертілді"
    return index(request, context)

def save_secondary_info_teacher(request):
    teacher = Teacher.objects.get(user__email=request.user)
    teacher.dareje = request.POST.get('dareje')
    teacher.phone_number = request.POST.get('phone_number')
    teacher.save()
    context = {

    }
    context['message'] = "Сәтті ақпараттар өзгертілді"
    return index(request, context)