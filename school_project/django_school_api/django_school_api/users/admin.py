# Django Admin Configuration for School API
# 
# Note: This project uses MongoEngine for data storage, which doesn't integrate
# directly with Django's admin interface. The admin interface here is primarily
# for Django's built-in User management (for admin access) and system administration.
#
# For managing your custom User data (stored in MongoDB), use the REST API endpoints:
# - POST /api/v1/users/create/ - Create new users
# - GET /api/v1/users/ - List all users  
# - GET /api/v1/users/{id}/ - Get specific user
# - PUT /api/v1/users/{id}/update/ - Update user
# - DELETE /api/v1/users/{id}/delete/ - Delete user
# - POST /api/v1/login/ - User authentication

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Customize the default User admin for better admin interface
class CustomUserAdmin(UserAdmin):
    """Enhanced User admin for Django's built-in User model"""
    
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('-date_joined',)
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

# Register the enhanced User admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Customize admin site headers
admin.site.site_header = "School API Administration"
admin.site.site_title = "School API Admin"
admin.site.index_title = "Welcome to School API Administration"
