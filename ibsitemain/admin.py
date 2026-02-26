from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Subject, NewsItem


# CustomUser Admin
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'full_name', 'role', 'is_active', 'enrollment_date', 'expiry_date', 'is_staff')
    list_filter = ('role', 'is_active', 'is_staff')
    search_fields = ('username', 'email', 'full_name')
    readonly_fields = ('last_login', 'date_joined')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('full_name', 'email', 'role', 'enrollment_date', 'expiry_date')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'full_name', 'role', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )

    actions = ['activate_users', 'deactivate_users']

    @admin.action(description="Activate selected users")
    def activate_users(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, f"{updated} user(s) activated.")
    
    @admin.action(description="Deactivate selected users")
    def deactivate_users(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, f"{updated} user(s) deactivated.")


# Subject Admin
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


# NewsItem Admin
@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'pub_date')
    list_filter = ('category', 'pub_date')
    search_fields = ('title', 'content')


   
from .models import CASProject

@admin.register(CASProject)
class CASProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "duration", "impact", "creativity", "activity", "service")
    list_filter = ("year", "creativity", "activity", "service")
    search_fields = ("title", "description", "impact")

