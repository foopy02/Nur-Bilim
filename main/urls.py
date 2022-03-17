from unicodedata import name
from django.urls import path,re_path
from . import views
# from .views import RegisterUser
from django.conf import settings
from django.views.static import serve
urlpatterns  = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register, name="register"),
    path('my_profile/', views.my_profile, name="profile"),
    path('profile/student/<str:email>', views.student_profile, name="student profile"),
    path('profile/teacher/<str:email>', views.teacher_profile, name="teacher profile"),
    path('profile/save_main_info', views.save_main_info, name="save main info"),
    path('profile/save_secondary_info', views.save_secondary_info_student, name="save secondary info student"),
    path('profile/save_secondary_info_teacher', views.save_secondary_info_teacher, name="save secondary info teacher"),
    path('course/create', views.create_course, name="create course"),
    path('course/add', views.add_to_course, name="add students"),
    path('course/<int:id>', views.course_page, name="course page"),
    path('course/create_practice', views.create_practice, name="create practice"),
    path('course/create_homework', views.create_homeworks, name="create homework"),
    path('course/create_lecture', views.create_lecture, name="create lecture"),
    path('course/<int:id>/students', views.students_of_course, name="students of course"),
    path('grade/create', views.create_grade, name="create grade"),
    path('grade/<int:id>/put', views.put_grade, name="change grade"),
    path('grade/get/<str:email>', views.get_grades, name="show grades"),
    path('course/add_student', views.add_student_to_course, name="add to course"),



    

]

if settings.DEBUG:
    urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),]