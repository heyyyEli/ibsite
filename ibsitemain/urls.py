"""
URL configuration for ibsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# ibsitemain/urls.py
from django.urls import path
from . import views
from .views import (
    ib_home, ib_subjects, ib_tips, ib_benefits_disadvantages,
    ib_tok, ib_ee, ib_cas, ib_news,
    login_view, logout_view, student_signup,
    CustomStudentPasswordResetView
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Homepage and main pages
    path('', ib_home, name='ib_home'),
    path('subjects/', ib_subjects, name='ib_subjects'),
    path('tips/', ib_tips, name='ib_tips'),
    path('ibinfo/', ib_benefits_disadvantages, name='ib_benefits_disadvantages'),
    path('tok/', ib_tok, name='ib_tok'),
    path('ee/', ib_ee, name='ib_ee'),
    path('cas/', ib_cas, name='ib_cas'),
    path('news/', ib_news, name='ib_news'),

    # Auth
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('student/signup/', student_signup, name='student_signup'),

    # Password reset
    path('password-reset/', CustomStudentPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]
