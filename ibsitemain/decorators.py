from django.http import HttpResponseForbidden
from functools import wraps
from django.contrib import admin

def role_required(role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.role == role:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("You do not have permission to access this page.")
        return _wrapped_view
    return decorator

student_required = role_required('student')
teacher_required = role_required('teacher')
admin_required = role_required('admin')



@admin.action(description='Activate selected users')
def activate_users(self, request, queryset):
    updated = queryset.update(is_active=True)
    self.message_user(request, f"{updated} user(s) activated.")

@admin.action(description='Deactivate selected users')
def deactivate_users(self, request, queryset):
    updated = queryset.update(is_active=False)
    self.message_user(request, f"{updated} user(s) deactivated.")