from django.db import models
from django.conf import settings

class Notification(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Student model
class Student(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Connect to User model
    grade = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)  # To track whether the student is active
    created_at = models.DateTimeField(auto_now_add=True)  # Track when the student was created
    updated_at = models.DateTimeField(auto_now=True)  # Track when the student data was last updated

    def __str__(self):
        return self.user.username


# Teacher model
class Teacher(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)   # Connect to User model
    subject = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)  # To track whether the teacher is active
    created_at = models.DateTimeField(auto_now_add=True)  # Track when the teacher was created
    updated_at = models.DateTimeField(auto_now=True)  # Track when the teacher data was last updated

    def __str__(self):
        return self.user.username


# Admin model (optional, since admin is a built-in Django feature)
class Admin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)   # Connect to User model
    is_active = models.BooleanField(default=True)  # Track whether the admin is active
    created_at = models.DateTimeField(auto_now_add=True)  # Track when the admin was created
    updated_at = models.DateTimeField(auto_now=True)  # Track when the admin data was last updated

    def __str__(self):
        return self.user.username
