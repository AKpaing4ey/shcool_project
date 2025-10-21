from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Role, Class, Attendance, Notice
from .serializers import (
    RoleSerializer, RoleCreateSerializer,
    ClassSerializer, ClassCreateSerializer,
    AttendanceSerializer, AttendanceCreateSerializer,
    NoticeSerializer, NoticeCreateSerializer
)
from .response_utils import success_response, error_response

class ModelPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# Role Views
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_roles(request):
    """Get all roles"""
    try:
        roles = Role.objects.all()
        paginator = ModelPagination()
        result_page = paginator.paginate_queryset(roles, request)
        serializer = RoleSerializer(result_page, many=True)
        
        paginated_response = paginator.get_paginated_response(serializer.data)
        roles_data = paginated_response.data['results']
        
        return success_response(
            data=roles_data,
            message="Roles retrieved successfully",
            http_status=200
        )
    except Exception as e:
        return error_response(
            message=f"Failed to retrieve roles: {str(e)}",
            http_status=500
        )

@api_view(['POST'])
@permission_classes([AllowAny])
def create_role(request):
    """Create a new role"""
    try:
        serializer = RoleCreateSerializer(data=request.data)
        if serializer.is_valid():
            role = serializer.save()
            response_serializer = RoleSerializer(role)
            return success_response(
                data=response_serializer.data,
                message="Role created successfully",
                http_status=201
            )
        else:
            return error_response(
                message="Validation failed",
                data=serializer.errors,
                http_status=400
            )
    except Exception as e:
        return error_response(
            message=f"Failed to create role: {str(e)}",
            http_status=500
        )

@api_view(['GET'])
@permission_classes([AllowAny])
def get_role_by_id(request, role_id):
    """Get role by ID"""
    try:
        role = Role.objects.get(id=role_id)
        serializer = RoleSerializer(role)
        return success_response(
            data=serializer.data,
            message="Role retrieved successfully",
            http_status=200
        )
    except Role.DoesNotExist:
        return error_response(
            message="Role not found",
            http_status=404
        )
    except Exception as e:
        return error_response(
            message=f"Failed to retrieve role: {str(e)}",
            http_status=500
        )

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_role(request, role_id):
    """Update role by ID"""
    try:
        role = Role.objects.get(id=role_id)
        serializer = RoleSerializer(role, data=request.data, partial=True)
        if serializer.is_valid():
            updated_role = serializer.save()
            response_serializer = RoleSerializer(updated_role)
            return success_response(
                data=response_serializer.data,
                message="Role updated successfully",
                http_status=200
            )
        else:
            return error_response(
                message="Validation failed",
                data=serializer.errors,
                http_status=400
            )
    except Role.DoesNotExist:
        return error_response(
            message="Role not found",
            http_status=404
        )
    except Exception as e:
        return error_response(
            message=f"Failed to update role: {str(e)}",
            http_status=500
        )

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_role(request, role_id):
    """Delete role by ID"""
    try:
        role = Role.objects.get(id=role_id)
        role.delete()
        return success_response(
            data=None,
            message="Role deleted successfully",
            http_status=200
        )
    except Role.DoesNotExist:
        return error_response(
            message="Role not found",
            http_status=404
        )
    except Exception as e:
        return error_response(
            message=f"Failed to delete role: {str(e)}",
            http_status=500
        )

# Class Views
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_classes(request):
    """Get all classes"""
    try:
        classes = Class.objects.all()
        paginator = ModelPagination()
        result_page = paginator.paginate_queryset(classes, request)
        serializer = ClassSerializer(result_page, many=True)
        
        paginated_response = paginator.get_paginated_response(serializer.data)
        classes_data = paginated_response.data['results']
        
        return success_response(
            data=classes_data,
            message="Classes retrieved successfully",
            http_status=200
        )
    except Exception as e:
        return error_response(
            message=f"Failed to retrieve classes: {str(e)}",
            http_status=500
        )

@api_view(['POST'])
@permission_classes([AllowAny])
def create_class(request):
    """Create a new class"""
    try:
        serializer = ClassCreateSerializer(data=request.data)
        if serializer.is_valid():
            class_obj = serializer.save()
            response_serializer = ClassSerializer(class_obj)
            return success_response(
                data=response_serializer.data,
                message="Class created successfully",
                http_status=201
            )
        else:
            return error_response(
                message="Validation failed",
                data=serializer.errors,
                http_status=400
            )
    except Exception as e:
        return error_response(
            message=f"Failed to create class: {str(e)}",
            http_status=500
        )

@api_view(['GET'])
@permission_classes([AllowAny])
def get_class_by_id(request, class_id):
    """Get class by ID"""
    try:
        class_obj = Class.objects.get(id=class_id)
        serializer = ClassSerializer(class_obj)
        return success_response(
            data=serializer.data,
            message="Class retrieved successfully",
            http_status=200
        )
    except Class.DoesNotExist:
        return error_response(
            message="Class not found",
            http_status=404
        )
    except Exception as e:
        return error_response(
            message=f"Failed to retrieve class: {str(e)}",
            http_status=500
        )

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_class(request, class_id):
    """Update class by ID"""
    try:
        class_obj = Class.objects.get(id=class_id)
        serializer = ClassSerializer(class_obj, data=request.data, partial=True)
        if serializer.is_valid():
            updated_class = serializer.save()
            response_serializer = ClassSerializer(updated_class)
            return success_response(
                data=response_serializer.data,
                message="Class updated successfully",
                http_status=200
            )
        else:
            return error_response(
                message="Validation failed",
                data=serializer.errors,
                http_status=400
            )
    except Class.DoesNotExist:
        return error_response(
            message="Class not found",
            http_status=404
        )
    except Exception as e:
        return error_response(
            message=f"Failed to update class: {str(e)}",
            http_status=500
        )

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_class(request, class_id):
    """Delete class by ID"""
    try:
        class_obj = Class.objects.get(id=class_id)
        class_obj.delete()
        return success_response(
            data=None,
            message="Class deleted successfully",
            http_status=200
        )
    except Class.DoesNotExist:
        return error_response(
            message="Class not found",
            http_status=404
        )
    except Exception as e:
        return error_response(
            message=f"Failed to delete class: {str(e)}",
            http_status=500
        )

# Attendance Views
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_attendances(request):
    """Get all attendances"""
    try:
        attendances = Attendance.objects.all()
        paginator = ModelPagination()
        result_page = paginator.paginate_queryset(attendances, request)
        serializer = AttendanceSerializer(result_page, many=True)
        
        paginated_response = paginator.get_paginated_response(serializer.data)
        attendances_data = paginated_response.data['results']
        
        return success_response(
            data=attendances_data,
            message="Attendances retrieved successfully",
            http_status=200
        )
    except Exception as e:
        return error_response(
            message=f"Failed to retrieve attendances: {str(e)}",
            http_status=500
        )

@api_view(['POST'])
@permission_classes([AllowAny])
def create_attendance(request):
    """Create a new attendance"""
    try:
        serializer = AttendanceCreateSerializer(data=request.data)
        if serializer.is_valid():
            attendance = serializer.save()
            response_serializer = AttendanceSerializer(attendance)
            return success_response(
                data=response_serializer.data,
                message="Attendance created successfully",
                http_status=201
            )
        else:
            return error_response(
                message="Validation failed",
                data=serializer.errors,
                http_status=400
            )
    except Exception as e:
        return error_response(
            message=f"Failed to create attendance: {str(e)}",
            http_status=500
        )

@api_view(['GET'])
@permission_classes([AllowAny])
def get_attendance_by_id(request, attendance_id):
    """Get attendance by ID"""
    try:
        attendance = Attendance.objects.get(id=attendance_id)
        serializer = AttendanceSerializer(attendance)
        return success_response(
            data=serializer.data,
            message="Attendance retrieved successfully",
            http_status=200
        )
    except Attendance.DoesNotExist:
        return error_response(
            message="Attendance not found",
            http_status=404
        )
    except Exception as e:
        return error_response(
            message=f"Failed to retrieve attendance: {str(e)}",
            http_status=500
        )

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_attendance(request, attendance_id):
    """Update attendance by ID"""
    try:
        attendance = Attendance.objects.get(id=attendance_id)
        serializer = AttendanceSerializer(attendance, data=request.data, partial=True)
        if serializer.is_valid():
            updated_attendance = serializer.save()
            response_serializer = AttendanceSerializer(updated_attendance)
            return success_response(
                data=response_serializer.data,
                message="Attendance updated successfully",
                http_status=200
            )
        else:
            return error_response(
                message="Validation failed",
                data=serializer.errors,
                http_status=400
            )
    except Attendance.DoesNotExist:
        return error_response(
            message="Attendance not found",
            http_status=404
        )
    except Exception as e:
        return error_response(
            message=f"Failed to update attendance: {str(e)}",
            http_status=500
        )

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_attendance(request, attendance_id):
    """Delete attendance by ID"""
    try:
        attendance = Attendance.objects.get(id=attendance_id)
        attendance.delete()
        return success_response(
            data=None,
            message="Attendance deleted successfully",
            http_status=200
        )
    except Attendance.DoesNotExist:
        return error_response(
            message="Attendance not found",
            http_status=404
        )
    except Exception as e:
        return error_response(
            message=f"Failed to delete attendance: {str(e)}",
            http_status=500
        )

# Notice Views
@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_notices(request):
    """Get all notices"""
    try:
        notices = Notice.objects.all()
        paginator = ModelPagination()
        result_page = paginator.paginate_queryset(notices, request)
        serializer = NoticeSerializer(result_page, many=True)
        
        paginated_response = paginator.get_paginated_response(serializer.data)
        notices_data = paginated_response.data['results']
        
        return success_response(
            data=notices_data,
            message="Notices retrieved successfully",
            http_status=200
        )
    except Exception as e:
        return error_response(
            message=f"Failed to retrieve notices: {str(e)}",
            http_status=500
        )

@api_view(['POST'])
@permission_classes([AllowAny])
def create_notice(request):
    """Create a new notice"""
    try:
        serializer = NoticeCreateSerializer(data=request.data)
        if serializer.is_valid():
            notice = serializer.save()
            response_serializer = NoticeSerializer(notice)
            return success_response(
                data=response_serializer.data,
                message="Notice created successfully",
                http_status=201
            )
        else:
            return error_response(
                message="Validation failed",
                data=serializer.errors,
                http_status=400
            )
    except Exception as e:
        return error_response(
            message=f"Failed to create notice: {str(e)}",
            http_status=500
        )

@api_view(['GET'])
@permission_classes([AllowAny])
def get_notice_by_id(request, notice_id):
    """Get notice by ID"""
    try:
        notice = Notice.objects.get(id=notice_id)
        serializer = NoticeSerializer(notice)
        return success_response(
            data=serializer.data,
            message="Notice retrieved successfully",
            http_status=200
        )
    except Notice.DoesNotExist:
        return error_response(
            message="Notice not found",
            http_status=404
        )
    except Exception as e:
        return error_response(
            message=f"Failed to retrieve notice: {str(e)}",
            http_status=500
        )

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_notice(request, notice_id):
    """Update notice by ID"""
    try:
        notice = Notice.objects.get(id=notice_id)
        serializer = NoticeSerializer(notice, data=request.data, partial=True)
        if serializer.is_valid():
            updated_notice = serializer.save()
            response_serializer = NoticeSerializer(updated_notice)
            return success_response(
                data=response_serializer.data,
                message="Notice updated successfully",
                http_status=200
            )
        else:
            return error_response(
                message="Validation failed",
                data=serializer.errors,
                http_status=400
            )
    except Notice.DoesNotExist:
        return error_response(
            message="Notice not found",
            http_status=404
        )
    except Exception as e:
        return error_response(
            message=f"Failed to update notice: {str(e)}",
            http_status=500
        )

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_notice(request, notice_id):
    """Delete notice by ID"""
    try:
        notice = Notice.objects.get(id=notice_id)
        notice.delete()
        return success_response(
            data=None,
            message="Notice deleted successfully",
            http_status=200
        )
    except Notice.DoesNotExist:
        return error_response(
            message="Notice not found",
            http_status=404
        )
    except Exception as e:
        return error_response(
            message=f"Failed to delete notice: {str(e)}",
            http_status=500
        )
