from django.contrib import admin
from .models import Notification, Student, Teacher, Admin

admin.site.register(Notification)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Admin)
