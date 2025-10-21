import jwt
from datetime import datetime, timedelta
from django.conf import settings

def generate_jwt_token(user):
    """
    Generate JWT token for user
    """
    payload = {
        'email': user.email,
        'name': user.name,
        'user_id': user.user_id,
        'exp': datetime.utcnow() + timedelta(seconds=settings.JWT_EXPIRATION_DELTA),
        'iat': datetime.utcnow()
    }
    
    token = jwt.encode(
        payload, 
        settings.JWT_SECRET_KEY, 
        algorithm=settings.JWT_ALGORITHM
    )
    
    return token

def verify_jwt_token(token):
    """
    Verify JWT token and return payload
    """
    try:
        payload = jwt.decode(
            token, 
            settings.JWT_SECRET_KEY, 
            algorithms=[settings.JWT_ALGORITHM]
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception('Token has expired')
    except jwt.InvalidTokenError:
        raise Exception('Invalid token')
