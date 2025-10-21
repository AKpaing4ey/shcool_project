from django.urls import path
from . import views
from . import additional_views
from . import nodejs_views

urlpatterns = [
    # Node.js equivalent routes (exact match)
    path('', nodejs_views.get_all_users_nodejs, name='get_all_users_nodejs'),
    path('sign_in/', nodejs_views.sign_in, name='sign_in'),
    path('sign_up/', nodejs_views.sign_up, name='sign_up'),
    path('update/', nodejs_views.update_user_nodejs, name='update_user_nodejs'),
    path('delete/', nodejs_views.delete_user_nodejs, name='delete_user_nodejs'),

    # Original Django REST API routes
    path('users/', views.get_all_users, name='get_all_users'),
    path('users/create/', views.create_user, name='create_user'),
    path('users/<int:user_id>/', views.get_user_by_id, name='get_user_by_id'),
    path('users/<int:user_id>/update/', views.update_user, name='update_user'),
    path('users/<int:user_id>/delete/', views.delete_user, name='delete_user'),
    path('users/email/<str:email>/', views.get_user_by_email, name='get_user_by_email'),

    # Authentication
    path('login/', views.login, name='login'),

    # Role CRUD operations
    path('roles/', additional_views.get_all_roles, name='get_all_roles'),
    path('roles/create/', additional_views.create_role, name='create_role'),
    path('roles/<str:role_id>/', additional_views.get_role_by_id, name='get_role_by_id'),
    path('roles/<str:role_id>/update/', additional_views.update_role, name='update_role'),
    path('roles/<str:role_id>/delete/', additional_views.delete_role, name='delete_role'),

    # Class CRUD operations
    path('classes/', additional_views.get_all_classes, name='get_all_classes'),
    path('classes/create/', additional_views.create_class, name='create_class'),
    path('classes/<str:class_id>/', additional_views.get_class_by_id, name='get_class_by_id'),
    path('classes/<str:class_id>/update/', additional_views.update_class, name='update_class'),
    path('classes/<str:class_id>/delete/', additional_views.delete_class, name='delete_class'),

    # Attendance CRUD operations
    path('attendances/', additional_views.get_all_attendances, name='get_all_attendances'),
    path('attendances/create/', additional_views.create_attendance, name='create_attendance'),
    path('attendances/<str:attendance_id>/', additional_views.get_attendance_by_id, name='get_attendance_by_id'),
    path('attendances/<str:attendance_id>/update/', additional_views.update_attendance, name='update_attendance'),
    path('attendances/<str:attendance_id>/delete/', additional_views.delete_attendance, name='delete_attendance'),

    # Notice CRUD operations
    path('notices/', additional_views.get_all_notices, name='get_all_notices'),
    path('notices/create/', additional_views.create_notice, name='create_notice'),
    path('notices/<str:notice_id>/', additional_views.get_notice_by_id, name='get_notice_by_id'),
    path('notices/<str:notice_id>/update/', additional_views.update_notice, name='update_notice'),
    path('notices/<str:notice_id>/delete/', additional_views.delete_notice, name='delete_notice'),
]
