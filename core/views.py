from django.shortcuts import render
from .models import Enrollment, Notification, Performance

# Student Dashboard
def student_dashboard(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    notifications = Notification.objects.filter(user=request.user)
    return render(request, 'core/student_dashboard.html', {
        'enrollments': enrollments,
        'notifications': notifications
    })

# Teacher Dashboard
def teacher_dashboard(request):
    # Add logic to show managed courses and student performances
    return render(request, 'core/teacher_dashboard.html')

# Admin Dashboard
def admin_dashboard(request):
    # Add logic for admin overview
    return render(request, 'core/admin_dashboard.html')
