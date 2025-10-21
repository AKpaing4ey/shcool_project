"""
Notice routes - equivalent to Node.js notice routes
"""
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Notice
from .response_utils import response

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_notices_admin(request):
    """GET / - equivalent to Node.js router.get("/", ...)"""
    try:
        notices = Notice.objects.all()
        notices_data = []
        for notice in notices:
            notice_dict = {
                'id': str(notice.id),
                'title': notice.title,
                'content': notice.content,
                'status': notice.status,
                'since': notice.since.isoformat() if notice.since else None
            }
            notices_data.append(notice_dict)
        
        return Response(response(notices_data, True))
    except Exception as error:
        return Response(response(error, False))

@api_view(['POST'])
@permission_classes([AllowAny])
def create_notice_admin(request):
    """POST / - equivalent to Node.js router.post("/", ...)"""
    try:
        notice = Notice(**request.data)
        notice.save()
        notice_data = {
            'id': str(notice.id),
            'title': notice.title,
            'content': notice.content,
            'status': notice.status,
            'since': notice.since.isoformat() if notice.since else None
        }
        return Response(response(notice_data, True))
    except Exception as error:
        return Response(response(error, False))

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_notice_admin(request):
    """PUT / - equivalent to Node.js router.put("/", ...)"""
    try:
        notice_id = request.data.get('id')
        notice = Notice.objects.get(id=notice_id)
        
        # Update fields
        if 'title' in request.data:
            notice.title = request.data['title']
        
        if 'content' in request.data:
            notice.content = request.data['content']
        
        if 'status' in request.data:
            notice.status = request.data['status']
        
        notice.save()
        notice_data = {
            'id': str(notice.id),
            'title': notice.title,
            'content': notice.content,
            'status': notice.status,
            'since': notice.since.isoformat() if notice.since else None
        }
        return Response(response(notice_data, True))
    except Notice.DoesNotExist:
        return Response(response("Notice not found", False))
    except Exception as error:
        return Response(response(error, False))

@api_view(['POST'])
@permission_classes([AllowAny])
def delete_notice_admin(request):
    """POST /delete - equivalent to Node.js router.post("/delete", ...)"""
    try:
        notice_id = request.data.get('id')
        notice = Notice.objects.get(id=notice_id)
        notice.delete()
        return Response(response({'deleted': True, 'id': notice_id}, True))
    except Notice.DoesNotExist:
        return Response(response("Notice not found", False))
    except Exception as error:
        return Response(response(error, False))
