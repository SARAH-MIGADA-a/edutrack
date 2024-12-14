from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .models import Notification, Student, Teacher

# Home page view (root URL)
def home(request):
    # Fetch notifications from the database to display on the homepage
    notifications = Notification.objects.all().order_by('-created_at')[:5]  # Fetch the latest 5 notifications
    context = {
        'notifications': notifications,
    }
    return render(request, 'core/home.html', context)


# Custom login view
class CustomLoginView(LoginView):
    template_name = 'core/login.html'  # Point to your login template

    def get_success_url(self):
        user = self.request.user
        print("DEBUG: User groups ->", user.groups.all())  # Log user groups for debugging

        if user.groups.filter(name='Students').exists():
            print("DEBUG: Redirecting to student dashboard")
            return '/student_dashboard/'
        elif user.groups.filter(name='Teachers').exists():
            print("DEBUG: Redirecting to teacher dashboard")
            return '/teacher_dashboard/'
        elif user.is_superuser or user.is_staff:
            print("DEBUG: Redirecting to admin dashboard")
            return '/admin_area/dashboard/'
        else:
            messages.error(self.request, 'Your account does not have a valid dashboard')
            print("DEBUG: Redirecting to login")
            return '/login/'


# Logout view
def user_logout(request):
    logout(request)
    return redirect('login')


# Admin dashboard view
@login_required(login_url='login')
def admin_dashboard(request):
    if not (request.user.is_superuser or request.user.is_staff):
        messages.error(request, 'You do not have permission to access this dashboard')
        return redirect('login')  # Redirect unauthorized users to login
    
    # Fetch all students and teachers for the admin to manage
    students = Student.objects.all()
    teachers = Teacher.objects.all()

    context = {
        'user': request.user,
        'students': students,
        'teachers': teachers,
    }
    return render(request, 'core/admin_dashboard.html', context)


# Student dashboard view
@login_required(login_url='login')
def student_dashboard(request):
    # Check if the user is part of the 'Students' group
    if not request.user.groups.filter(name='Students').exists():
        messages.error(request, 'You do not have permission to access this dashboard')
        return redirect('login')  # Redirect unauthorized users to login

    # Fetch student-specific data from the database
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        student = None  # Handle the case where the student is not found

    context = {
        'student': student,
    }
    return render(request, 'core/student_dashboard.html', context)


# Teacher dashboard view
@login_required(login_url='login')
def teacher_dashboard(request):
    # Check if the user is part of the 'Teachers' group
    if not request.user.groups.filter(name='Teachers').exists():
        messages.error(request, 'You do not have permission to access this dashboard')
        return redirect('login')  # Redirect unauthorized users to login

    # Fetch teacher-specific data from the database
    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        teacher = None  # Handle the case where the teacher is not found

    context = {
        'teacher': teacher,
    }
    return render(request, 'core/teacher_dashboard.html', context)
