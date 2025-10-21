"""
Dashboard routes - equivalent to Node.js dashboard routes
"""
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import User, Role, Class, Attendance, Notice
from .response_utils import response

@api_view(['GET'])
@permission_classes([AllowAny])
def get_dashboard_stats(request):
    """Get dashboard statistics - admin route"""
    try:
        # Get counts for each model
        total_users = User.objects.count()
        total_roles = Role.objects.count()
        total_classes = Class.objects.count()
        total_attendances = Attendance.objects.count()
        total_notices = Notice.objects.count()
        
        # Get active users
        active_users = User.objects.filter(status=True).count()
        
        # Get active notices
        active_notices = Notice.objects.filter(status=True).count()
        
        # Get recent data (last 7 days)
        from datetime import datetime, timedelta
        week_ago = datetime.utcnow() - timedelta(days=7)
        
        recent_users = User.objects.filter(since__gte=week_ago).count()
        recent_attendances = Attendance.objects.filter(since__gte=week_ago).count()
        
        dashboard_data = {
            'total_users': total_users,
            'active_users': active_users,
            'total_roles': total_roles,
            'total_classes': total_classes,
            'total_attendances': total_attendances,
            'total_notices': total_notices,
            'active_notices': active_notices,
            'recent_users': recent_users,
            'recent_attendances': recent_attendances
        }
        
        return Response({'con': True, 'data': dashboard_data, 'msg': 'Dashboard stats retrieved successfully'})
    except Exception as error:
        return Response({'con': False, 'data': str(error), 'msg': 'Failed to get dashboard stats'})

@api_view(['GET'])
@permission_classes([AllowAny])
def get_recent_activities(request):
    """Get recent activities - admin route"""
    try:
        from datetime import datetime, timedelta
        week_ago = datetime.utcnow() - timedelta(days=7)
        
        # Get recent users
        recent_users = User.objects.filter(since__gte=week_ago).order_by('-since')[:5]
        users_data = []
        for user in recent_users:
            users_data.append({
                'id': user.user_id,
                'name': user.name,
                'email': user.email,
                'since': user.since.isoformat() if user.since else None
            })
        
        # Get recent attendances
        recent_attendances = Attendance.objects.filter(since__gte=week_ago).order_by('-since')[:5]
        attendances_data = []
        for attendance in recent_attendances:
            attendances_data.append({
                'id': str(attendance.id),
                'user_name': attendance.user.name if attendance.user else None,
                'class_name': attendance.class_obj.name if attendance.class_obj else None,
                'checkIn_time': attendance.checkIn_time.isoformat() if attendance.checkIn_time else None,
                'since': attendance.since.isoformat() if attendance.since else None
            })
        
        # Get recent notices
        recent_notices = Notice.objects.filter(since__gte=week_ago).order_by('-since')[:5]
        notices_data = []
        for notice in recent_notices:
            notices_data.append({
                'id': str(notice.id),
                'title': notice.title,
                'status': notice.status,
                'since': notice.since.isoformat() if notice.since else None
            })
        
        activities_data = {
            'recent_users': users_data,
            'recent_attendances': attendances_data,
            'recent_notices': notices_data
        }
        
        return Response({'con': True, 'data': activities_data, 'msg': 'Recent activities retrieved successfully'})
    except Exception as error:
        return Response({'con': False, 'data': str(error), 'msg': 'Failed to get recent activities'})
