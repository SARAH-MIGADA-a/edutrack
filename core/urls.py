from django.contrib import admin
from django.urls import path
from edutrack.views import (
    home,
    CustomLoginView,
    user_logout,
    admin_dashboard,
    student_dashboard,
    teacher_dashboard,
)

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),  # Custom login view
    path('logout/', user_logout, name='logout'),  # Logout view
    path('admin_area/dashboard/', admin_dashboard, name='admin_dashboard'),  # Admin dashboard
    path('student_dashboard/', student_dashboard, name='student_dashboard'),  # Student dashboard
    path('teacher_dashboard/', teacher_dashboard, name='teacher_dashboard'),  # Teacher dashboard
]