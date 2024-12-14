from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrator'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('parent', 'Parent')
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    email = models.EmailField(_('email address'), unique=True)

    def __str__(self):
        return self.username

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    parent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    grade = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    present = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.student} - {self.date}"
    
class Course(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'})
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} in {self.course.name}"

class Performance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='performances')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='performances')
    grade = models.FloatField()
    feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.course.name} - {self.grade}"


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message[:20]}"
