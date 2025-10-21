"""
Django views matching Node.js user.js routes exactly
"""
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .user_db import all, save, update, find_user_email, remove_user
from .pass_helper import encrypt, compare
from .jwt_utils import generate_jwt_token
from .response_utils import response
import json

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_users_nodejs(request):
    """
    GET / - equivalent to Node.js router.get("/", ...)
    """
    try:
        result = all()
        # Convert MongoEngine objects to dictionaries
        users_data = []
        for user in result:
            user_dict = {
                'user_id': user.user_id,
                'email': user.email,
                'name': user.name,
                'role_id': str(user.role_id.id) if user.role_id else None,
                'address': user.address,
                'status': user.status,
                'phone': user.phone,
                'student_id': user.student_id,
                'since': user.since.isoformat() if user.since else None
            }
            users_data.append(user_dict)
        
        return Response(response(users_data, True))
    except Exception as error:
        return Response(response(error, False))

@api_view(['POST'])
@permission_classes([AllowAny])
def sign_in(request):
    """
    POST /sign_in - equivalent to Node.js router.post("/sign_in", ...)
    """
    try:
        email = request.data.get('email')
        password = request.data.get('password')
        
        result = find_user_email(email)
        
        # Compare password
        password_match = compare(password, result.password)
        
        if password_match:
            payload = {'email': result.email, 'name': result.name}
            token = generate_jwt_token(result)
            
            # Get role object if exists
            role_data = None
            if result.role_id:
                role_data = {
                    'id': str(result.role_id.id),
                    'name': result.role_id.name,
                    'since': result.role_id.since.isoformat() if result.role_id.since else None
                }
            
            user_data = {
                'user_id': result.user_id,
                'email': result.email,
                'name': result.name,
                'role': role_data,
                'address': result.address,
                'status': result.status,
                'phone': result.phone,
                'student_id': result.student_id,
                'since': result.since.isoformat() if result.since else None
            }
            
            return Response({
                'con': True,
                'token': token,
                'data': user_data,
                'msg': 'Login Successful!'
            })
        else:
            return Response({'con': False, 'msg': 'Password Wrong'})
            
    except Exception as error:
        return Response({'con': False, 'data': str(error), 'msg': 'Error, Email not Found'})

@api_view(['POST'])
@permission_classes([AllowAny])
def sign_up(request):
    """
    POST /sign_up - equivalent to Node.js router.post("/sign_up", ...)
    """
    try:
        phone = request.data.get('phone')
        email = request.data.get('email')
        password = request.data.get('password')
        role_id = request.data.get('role_id')
        name = request.data.get('name')
        address = request.data.get('address')
        
        # Encrypt password
        encrypted_password = encrypt(password)
        
        obj = {
            'phone': phone,
            'email': email,
            'password': encrypted_password,
            'role_id': role_id,
            'name': name,
            'address': address
        }
        
        data = save(obj)
        
        user_data = {
            'user_id': data.user_id,
            'email': data.email,
            'name': data.name,
            'role_id': str(data.role_id.id) if data.role_id else None,
            'address': data.address,
            'status': data.status,
            'phone': data.phone,
            'student_id': data.student_id,
            'since': data.since.isoformat() if data.since else None
        }
        
        return Response({'con': True, 'data': user_data, 'msg': 'Save'})
        
    except Exception as error:
        return Response({'con': False, 'data': str(error), 'msg': 'User Save Error'})

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_user_nodejs(request):
    """
    PUT / - equivalent to Node.js router.put("/", ...)
    """
    try:
        result = update(request.data)
        
        user_data = {
            'user_id': result.user_id,
            'email': result.email,
            'name': result.name,
            'role_id': str(result.role_id.id) if result.role_id else None,
            'address': result.address,
            'status': result.status,
            'phone': result.phone,
            'student_id': result.student_id,
            'since': result.since.isoformat() if result.since else None
        }
        
        return Response({'con': True, 'data': user_data, 'msg': 'Update Successfully!'})
        
    except Exception as error:
        error_str = str(error)
        if 'duplicate' in error_str.lower() or 'unique' in error_str.lower():
            return Response({'con': False, 'data': error_str, 'msg': 'Unique key error in User data'})
        else:
            return Response({'con': False, 'data': error_str, 'msg': 'Error Update in User data'})

@api_view(['POST'])
@permission_classes([AllowAny])
def delete_user_nodejs(request):
    """
    POST /delete - equivalent to Node.js router.post("/delete", ...)
    """
    try:
        user_id = request.data.get('user_id')
        result = remove_user(user_id)
        return Response(response(result, True))
    except Exception as error:
        return Response(response(error, False))
