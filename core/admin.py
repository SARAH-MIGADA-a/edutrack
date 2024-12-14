from django.contrib import admin
from .models import User, Student, Attendance, Course, Enrollment, Performance, Notification

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')  # Columns displayed in the list view
    search_fields = ('username', 'email', 'role')  # Search functionality for these fields
    list_filter = ('role',)  # Filter users by their roles

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'parent', 'grade')  # Columns displayed in the list view
    search_fields = ('user__username', 'grade')  # Search students by username and grade
    list_filter = ('grade',)  # Filter students by grade

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'present')  # Columns displayed in the list view
    search_fields = ('student__user__username', 'date')  # Search by student's username or date
    list_filter = ('date', 'present')  # Filter attendance records by date or presence status

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'teacher', 'created_at')  # Display course details
    search_fields = ('name', 'code', 'teacher__username')  # Search by course name, code, or teacher's username
    list_filter = ('teacher',)  # Filter courses by teacher

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrolled_at')  # Show enrollment details
    search_fields = ('student__user__username', 'course__name')  # Search by student's username or course name
    list_filter = ('enrolled_at',)  # Filter enrollments by enrollment date

@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'grade')  # Display performance details
    search_fields = ('student__user__username', 'course__name')  # Search by student's username or course name
    list_filter = ('grade',)  # Filter performances by grade

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at', 'is_read')  # Show notification details
    search_fields = ('user__username', 'message')  # Search by username or notification content
    list_filter = ('created_at', 'is_read')  # Filter notifications by date or read status


