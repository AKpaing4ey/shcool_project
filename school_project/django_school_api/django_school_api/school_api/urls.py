"""
URL configuration for school_api project.
"""
from django.contrib import admin
from django.urls import path, include
from users.admin_routes import admin_urlpatterns

urlpatterns = [
    path('django-admin/', admin.site.urls),  # Changed Django admin to avoid conflict
    path('api/v1/', include('users.urls')),
    # Admin routes - equivalent to Node.js app.use("/admin", adminRoute)
    path('admin/', include(admin_urlpatterns)),
]
