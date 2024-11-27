from django.contrib import admin
from .models import User, Student, Attendance

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'parent', 'grade')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'present')