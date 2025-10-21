"""
Attendance routes - equivalent to Node.js attendance routes
"""
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Attendance, User, Class
from .response_utils import response

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_attendances_admin(request):
    """GET / - equivalent to Node.js router.get("/", ...)"""
    try:
        attendances = Attendance.objects.all()
        attendances_data = []
        for attendance in attendances:
            attendance_dict = {
                'id': str(attendance.id),
                'user': str(attendance.user.user_id) if attendance.user else None,
                'user_name': attendance.user.name if attendance.user else None,
                'approve_by': str(attendance.approve_by.user_id) if attendance.approve_by else None,
                'approve_by_name': attendance.approve_by.name if attendance.approve_by else None,
                'class_obj': str(attendance.class_obj.id) if attendance.class_obj else None,
                'class_name': attendance.class_obj.name if attendance.class_obj else None,
                'checkIn_time': attendance.checkIn_time.isoformat() if attendance.checkIn_time else None,
                'checkOut_time': attendance.checkOut_time.isoformat() if attendance.checkOut_time else None,
                'since': attendance.since.isoformat() if attendance.since else None
            }
            attendances_data.append(attendance_dict)
        
        return Response(response(attendances_data, True))
    except Exception as error:
        return Response(response(error, False))

@api_view(['POST'])
@permission_classes([AllowAny])
def create_attendance_admin(request):
    """POST / - equivalent to Node.js router.post("/", ...)"""
    try:
        # Create a copy of request data to modify
        data = request.data.copy()
        
        # Handle user reference
        user_id = data.get('user')
        if user_id:
            try:
                user = User.objects.get(user_id=user_id)
                data['user'] = user
            except User.DoesNotExist:
                return Response(response("User not found", False))
        
        # Handle approve_by reference
        approve_by_id = data.get('approve_by')
        if approve_by_id:
            try:
                approve_by = User.objects.get(user_id=approve_by_id)
                data['approve_by'] = approve_by
            except User.DoesNotExist:
                pass
        
        # Handle class reference
        class_id = data.get('class_obj')
        if class_id:
            try:
                class_obj = Class.objects.get(id=class_id)
                data['class_obj'] = class_obj
            except Class.DoesNotExist:
                return Response(response("Class not found", False))
        
        # Handle datetime fields - convert string to datetime if needed
        from datetime import datetime
        if 'checkIn_time' in data and isinstance(data['checkIn_time'], str):
            try:
                data['checkIn_time'] = datetime.fromisoformat(data['checkIn_time'].replace('Z', '+00:00'))
            except ValueError:
                return Response(response("Invalid checkIn_time format. Use ISO format: YYYY-MM-DDTHH:MM:SS", False))
        
        if 'checkOut_time' in data and isinstance(data['checkOut_time'], str):
            try:
                data['checkOut_time'] = datetime.fromisoformat(data['checkOut_time'].replace('Z', '+00:00'))
            except ValueError:
                return Response(response("Invalid checkOut_time format. Use ISO format: YYYY-MM-DDTHH:MM:SS", False))
        
        attendance = Attendance(**data)
        attendance.save()
        
        attendance_data = {
            'id': str(attendance.id),
            'user': str(attendance.user.user_id) if attendance.user else None,
            'user_name': attendance.user.name if attendance.user else None,
            'approve_by': str(attendance.approve_by.user_id) if attendance.approve_by else None,
            'approve_by_name': attendance.approve_by.name if attendance.approve_by else None,
            'class_obj': str(attendance.class_obj.id) if attendance.class_obj else None,
            'class_name': attendance.class_obj.name if attendance.class_obj else None,
            'checkIn_time': attendance.checkIn_time.isoformat() if attendance.checkIn_time else None,
            'checkOut_time': attendance.checkOut_time.isoformat() if attendance.checkOut_time else None,
            'since': attendance.since.isoformat() if attendance.since else None
        }
        
        return Response(response(attendance_data, True))
    except Exception as error:
        return Response(response(str(error), False))

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_attendance_admin(request):
    """PUT / - equivalent to Node.js router.put("/", ...)"""
    try:
        attendance_id = request.data.get('id')
        attendance = Attendance.objects.get(id=attendance_id)
        
        # Update fields
        if 'user' in request.data:
            user_id = request.data.get('user')
            if user_id:
                try:
                    user = User.objects.get(user_id=user_id)
                    attendance.user = user
                except User.DoesNotExist:
                    return Response(response("User not found", False))
        
        if 'approve_by' in request.data:
            approve_by_id = request.data.get('approve_by')
            if approve_by_id:
                try:
                    approve_by = User.objects.get(user_id=approve_by_id)
                    attendance.approve_by = approve_by
                except User.DoesNotExist:
                    pass
        
        if 'class_obj' in request.data:
            class_id = request.data.get('class_obj')
            if class_id:
                try:
                    class_obj = Class.objects.get(id=class_id)
                    attendance.class_obj = class_obj
                except Class.DoesNotExist:
                    return Response(response("Class not found", False))
        
        if 'checkIn_time' in request.data:
            attendance.checkIn_time = request.data['checkIn_time']
        
        if 'checkOut_time' in request.data:
            attendance.checkOut_time = request.data['checkOut_time']
        
        attendance.save()
        
        attendance_data = {
            'id': str(attendance.id),
            'user': str(attendance.user.user_id) if attendance.user else None,
            'user_name': attendance.user.name if attendance.user else None,
            'approve_by': str(attendance.approve_by.user_id) if attendance.approve_by else None,
            'approve_by_name': attendance.approve_by.name if attendance.approve_by else None,
            'class_obj': str(attendance.class_obj.id) if attendance.class_obj else None,
            'class_name': attendance.class_obj.name if attendance.class_obj else None,
            'checkIn_time': attendance.checkIn_time.isoformat() if attendance.checkIn_time else None,
            'checkOut_time': attendance.checkOut_time.isoformat() if attendance.checkOut_time else None,
            'since': attendance.since.isoformat() if attendance.since else None
        }
        
        return Response(response(attendance_data, True))
    except Attendance.DoesNotExist:
        return Response(response("Attendance not found", False))
    except Exception as error:
        return Response(response(error, False))

@api_view(['POST'])
@permission_classes([AllowAny])
def delete_attendance_admin(request):
    """POST /delete - equivalent to Node.js router.post("/delete", ...)"""
    try:
        attendance_id = request.data.get('id')
        attendance = Attendance.objects.get(id=attendance_id)
        attendance.delete()
        return Response(response({'deleted': True, 'id': attendance_id}, True))
    except Attendance.DoesNotExist:
        return Response(response("Attendance not found", False))
    except Exception as error:
        return Response(response(error, False))
