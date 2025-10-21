from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer, UserCreateSerializer, UserUpdateSerializer, UserWithRoleSerializer
from .pass_helper import compare
from .jwt_utils import generate_jwt_token
from .response_utils import success_response, error_response

class UserPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_users(request):
    """
    Get all users with pagination
    Equivalent to: all() function in Node.js
    """
    try:
        users = User.objects.all()
        paginator = UserPagination()
        result_page = paginator.paginate_queryset(users, request)
        serializer = UserSerializer(result_page, many=True)
        
        # Get paginated response data
        paginated_response = paginator.get_paginated_response(serializer.data)
        users_data = paginated_response.data['results']
        
        return success_response(
            data=users_data,
            message="Users retrieved successfully",
            http_status=200
        )
    except Exception as e:
        return error_response(
            message=f"Failed to retrieve users: {str(e)}",
            http_status=500
        )

@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    """
    Create a new user
    Equivalent to: save() function in Node.js
    """
    try:
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response_serializer = UserSerializer(user)
            return success_response(
                data=response_serializer.data,
                message="User created successfully",
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
            message=f"Failed to create user: {str(e)}",
            http_status=500
        )

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_user(request, user_id):
    """
    Update user by user_id
    Equivalent to: update() function in Node.js
    """
    try:
        user = User.objects.get(user_id=user_id)
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            updated_user = serializer.save()
            response_serializer = UserSerializer(updated_user)
            return success_response(
                data=response_serializer.data,
                message="User updated successfully",
                http_status=200
            )
        else:
            return error_response(
                message="Validation failed",
                data=serializer.errors,
                http_status=400
            )
    except User.DoesNotExist:
        return error_response(
            message="User not found",
            http_status=404
        )
    except Exception as e:
        return error_response(
            message=f"Failed to update user: {str(e)}",
            http_status=500
        )

@api_view(['GET'])
@permission_classes([AllowAny])
def get_user_by_id(request, user_id):
    """
    Get user by user_id
    Equivalent to: find_user() function in Node.js
    """
    try:
        user = User.objects.get(user_id=user_id)
        serializer = UserSerializer(user)
        return success_response(
            data=serializer.data,
            message="User retrieved successfully",
            http_status=200
        )
    except User.DoesNotExist:
        return error_response(
            message="User not found",
            http_status=404
        )
    except Exception as e:
        return error_response(
            message=f"Failed to retrieve user: {str(e)}",
            http_status=500
        )

@api_view(['GET'])
@permission_classes([AllowAny])
def get_user_by_email(request, email):
    """
    Get user by email
    Equivalent to: find_user_email() function in Node.js
    """
    try:
        user = User.objects.get(email=email)
        serializer = UserSerializer(user)
        return success_response(
            data=serializer.data,
            message="User retrieved successfully",
            http_status=200
        )
    except User.DoesNotExist:
        return error_response(
            message="User not found",
            http_status=404
        )
    except Exception as e:
        return error_response(
            message=f"Failed to retrieve user: {str(e)}",
            http_status=500
        )

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_user(request, user_id):
    """
    Delete user by user_id
    Equivalent to: remove_user() function in Node.js
    """
    try:
        user = User.objects.get(user_id=user_id)
        user.delete()
        return success_response(
            data=None,
            message="User deleted successfully",
            http_status=200
        )
    except User.DoesNotExist:
        return error_response(
            message="User not found",
            http_status=404
        )
    except Exception as e:
        return error_response(
            message=f"Failed to delete user: {str(e)}",
            http_status=500
        )

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """
    Login endpoint to generate JWT token
    """
    try:
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not email or not password:
            return error_response(
                message="Email and password are required",
                http_status=400
            )
        
        user = User.objects.get(email=email)
        # Compare password using the helper function
        if compare(password, user.password):
            token = generate_jwt_token(user)
            user_data = UserWithRoleSerializer(user).data
            login_data = {
                "token": token,
                "user": user_data
            }
            return success_response(
                data=login_data,
                message="Login successful",
                http_status=200
            )
        else:
            return error_response(
                message="Invalid credentials",
                http_status=401
            )
    except User.DoesNotExist:
        return error_response(
            message="User not found",
            http_status=404
        )
    except Exception as e:
        return error_response(
            message=f"Login failed: {str(e)}",
            http_status=500
        )
