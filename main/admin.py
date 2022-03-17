from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from main.models import *

# Register your models here.

class MyUserAdmin(BaseUserAdmin):
    list_display=('email', 'role','date_joined','last_login', 'is_admin','is_active')
    search_fields=('email','role')
    readonly_fields=('date_joined','last_login')
    filter_horizontal=()
    list_filter = ('role',)
    fieldsets=()

    add_fieldsets=  (
        (None, {
            'classes':('wide'),
            'fields':('email','role','password1','password2')
        }),
    )

    ordering=('email',)
    
admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Homework)
admin.site.register(Lecture)
admin.site.register(Practice)
admin.site.register(Grade)