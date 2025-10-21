import jwt
from django.conf import settings
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from users.models import User

class UserWrapper:
    """
    Wrapper to make MongoEngine User compatible with Django's authentication system
    """
    def __init__(self, mongo_user):
        self._mongo_user = mongo_user
        # Add Django User attributes
        self.is_authenticated = True
        self.is_anonymous = False
        
    def __getattr__(self, name):
        # Delegate attribute access to the underlying MongoEngine user
        return getattr(self._mongo_user, name)
    
    def __str__(self):
        return str(self._mongo_user)

class JWTAuthentication(BaseAuthentication):
    """
    Custom JWT authentication class
    """
    
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        
        if not auth_header:
            return None
            
        try:
            # Extract token from "Bearer <token>"
            token = auth_header.split(' ')[1]
        except IndexError:
            return None
            
        try:
            # Decode JWT token
            payload = jwt.decode(
                token, 
                settings.JWT_SECRET_KEY, 
                algorithms=[settings.JWT_ALGORITHM]
            )
            
            # Get user from payload
            email = payload.get('email')
            name = payload.get('name')
            
            if not email or not name:
                raise exceptions.AuthenticationFailed('Invalid token payload')
                
            # Find user by email
            try:
                mongo_user = User.objects.get(email=email)
                if mongo_user.name != name:
                    raise exceptions.AuthenticationFailed('Invalid user data')
                # Wrap the MongoEngine user to make it compatible with Django
                user = UserWrapper(mongo_user)
                return (user, token)
            except User.DoesNotExist:
                raise exceptions.AuthenticationFailed('User not found')
                
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token has expired')
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed('Invalid token')
    
    def authenticate_header(self, request):
        return 'Bearer'
