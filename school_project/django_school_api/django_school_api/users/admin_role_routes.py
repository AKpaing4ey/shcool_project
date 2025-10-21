"""
Role routes - equivalent to Node.js role routes
"""
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Role
from .response_utils import response

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_roles_admin(request):
    """GET / - equivalent to Node.js router.get("/", ...)"""
    try:
        roles = Role.objects.all()
        roles_data = []
        for role in roles:
            role_dict = {
                'id': str(role.id),
                'name': role.name,
                'since': role.since.isoformat() if role.since else None
            }
            roles_data.append(role_dict)
        
        return Response(response(roles_data, True))
    except Exception as error:
        return Response(response(error, False))

@api_view(['POST'])
@permission_classes([AllowAny])
def create_role_admin(request):
    """POST / - equivalent to Node.js router.post("/", ...)"""
    try:
        role = Role(**request.data)
        role.save()
        role_data = {
            'id': str(role.id),
            'name': role.name,
            'since': role.since.isoformat() if role.since else None
        }
        return Response(response(role_data, True))
    except Exception as error:
        return Response(response(error, False))

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_role_admin(request):
    """PUT / - equivalent to Node.js router.put("/", ...)"""
    try:
        role_id = request.data.get('id')
        role = Role.objects.get(id=role_id)
        
        # Update fields
        if 'name' in request.data:
            role.name = request.data['name']
        
        role.save()
        role_data = {
            'id': str(role.id),
            'name': role.name,
            'since': role.since.isoformat() if role.since else None
        }
        return Response(response(role_data, True))
    except Role.DoesNotExist:
        return Response(response("Role not found", False))
    except Exception as error:
        return Response(response(error, False))

@api_view(['POST'])
@permission_classes([AllowAny])
def delete_role_admin(request):
    """POST /delete - equivalent to Node.js router.post("/delete", ...)"""
    try:
        role_id = request.data.get('id')
        role = Role.objects.get(id=role_id)
        role.delete()
        return Response(response({'deleted': True, 'id': role_id}, True))
    except Role.DoesNotExist:
        return Response(response("Role not found", False))
    except Exception as error:
        return Response(response(error, False))
