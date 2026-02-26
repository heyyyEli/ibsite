from django.contrib.auth.forms import PasswordResetForm
from .models import CustomUser

class StudentPasswordResetForm(PasswordResetForm):
    def get_users(self, email):
        active_students = CustomUser.objects.filter(email__iexact=email, is_active=True, role='student')
        return (user for user in active_students if user.has_usable_password())
