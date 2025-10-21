"""
Admin routes - equivalent to Node.js admin routes structure
"""
from django.urls import path
from . import admin_role_routes
from . import admin_notice_routes
from . import admin_class_routes
from . import admin_attendance_routes
from . import admin_dashboard_routes
from . import nodejs_views

# Admin URL patterns - equivalent to Node.js admin routes
admin_urlpatterns = [
    # User routes (using existing nodejs_views) - matches Node.js user routes exactly
    path('api/v_1/user/', nodejs_views.get_all_users_nodejs, name='admin_get_all_users'),
    path('api/v_1/user/sign_in/', nodejs_views.sign_in, name='admin_sign_in'),
    path('api/v_1/user/sign_up/', nodejs_views.sign_up, name='admin_sign_up'),
    path('api/v_1/user/update/', nodejs_views.update_user_nodejs, name='admin_update_user'),
    path('api/v_1/user/delete/', nodejs_views.delete_user_nodejs, name='admin_delete_user'),
    
    # Role routes - matches Node.js role routes exactly
    path('api/v_1/role/', admin_role_routes.get_all_roles_admin, name='admin_get_all_roles'),
    path('api/v_1/role/create/', admin_role_routes.create_role_admin, name='admin_create_role'),
    path('api/v_1/role/update/', admin_role_routes.update_role_admin, name='admin_update_role'),
    path('api/v_1/role/delete/', admin_role_routes.delete_role_admin, name='admin_delete_role'),
    
    # Notice routes - matches Node.js notice routes exactly
    path('api/v_1/notice/', admin_notice_routes.get_all_notices_admin, name='admin_get_all_notices'),
    path('api/v_1/notice/create/', admin_notice_routes.create_notice_admin, name='admin_create_notice'),
    path('api/v_1/notice/update/', admin_notice_routes.update_notice_admin, name='admin_update_notice'),
    path('api/v_1/notice/delete/', admin_notice_routes.delete_notice_admin, name='admin_delete_notice'),
    
    # Attendance routes - matches Node.js attendance routes exactly
    path('api/v_1/attendance/', admin_attendance_routes.get_all_attendances_admin, name='admin_get_all_attendances'),
    path('api/v_1/attendance/create/', admin_attendance_routes.create_attendance_admin, name='admin_create_attendance'),
    path('api/v_1/attendance/update/', admin_attendance_routes.update_attendance_admin, name='admin_update_attendance'),
    path('api/v_1/attendance/delete/', admin_attendance_routes.delete_attendance_admin, name='admin_delete_attendance'),
    
    # Class routes - matches Node.js class routes exactly
    path('api/v_1/class/', admin_class_routes.get_all_classes_admin, name='admin_get_all_classes'),
    path('api/v_1/class/create/', admin_class_routes.create_class_admin, name='admin_create_class'),
    path('api/v_1/class/update/', admin_class_routes.update_class_admin, name='admin_update_class'),
    path('api/v_1/class/delete/', admin_class_routes.delete_class_admin, name='admin_delete_class'),
    
    # Dashboard routes
    path('api/v_1/dashboard/stats/', admin_dashboard_routes.get_dashboard_stats, name='admin_dashboard_stats'),
    path('api/v_1/dashboard/activities/', admin_dashboard_routes.get_recent_activities, name='admin_recent_activities'),
]
