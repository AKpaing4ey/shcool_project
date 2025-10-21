"""
Class routes - equivalent to Node.js class routes
"""
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Class
from .response_utils import response

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_classes_admin(request):
    """GET / - equivalent to Node.js router.get("/", ...)"""
    try:
        classes = Class.objects.all()
        classes_data = []
        for class_obj in classes:
            class_dict = {
                'id': str(class_obj.id),
                'name': class_obj.name,
                'since': class_obj.since.isoformat() if class_obj.since else None
            }
            classes_data.append(class_dict)
        
        return Response(response(classes_data, True))
    except Exception as error:
        return Response(response(error, False))

@api_view(['POST'])
@permission_classes([AllowAny])
def create_class_admin(request):
    """POST / - equivalent to Node.js router.post("/", ...)"""
    try:
        class_obj = Class(**request.data)
        class_obj.save()
        class_data = {
            'id': str(class_obj.id),
            'name': class_obj.name,
            'since': class_obj.since.isoformat() if class_obj.since else None
        }
        return Response(response(class_data, True))
    except Exception as error:
        return Response(response(error, False))

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_class_admin(request):
    """PUT / - equivalent to Node.js router.put("/", ...)"""
    try:
        class_id = request.data.get('id')
        class_obj = Class.objects.get(id=class_id)
        
        # Update fields
        if 'name' in request.data:
            class_obj.name = request.data['name']
        
        class_obj.save()
        class_data = {
            'id': str(class_obj.id),
            'name': class_obj.name,
            'since': class_obj.since.isoformat() if class_obj.since else None
        }
        return Response(response(class_data, True))
    except Class.DoesNotExist:
        return Response(response("Class not found", False))
    except Exception as error:
        return Response(response(error, False))

@api_view(['POST'])
@permission_classes([AllowAny])
def delete_class_admin(request):
    """POST /delete - equivalent to Node.js router.post("/delete", ...)"""
    try:
        class_id = request.data.get('class_id')
        class_obj = Class.objects.get(id=class_id)
        class_obj.delete()
        return Response(response({'deleted': True, 'id': class_id}, True))
    except Class.DoesNotExist:
        return Response(response("Class not found", False))
    except Exception as error:
        return Response(response(error, False))
