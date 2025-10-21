"""
Database functions matching Node.js user.js database
"""
from datetime import datetime
from .models import User, Role
from .response_utils import response

def all():
    """Get all users - equivalent to Node.js all() function"""
    try:
        users = User.objects.all()
        return users
    except Exception as e:
        raise e

def save(obj):
    """Save user - equivalent to Node.js save() function"""
    try:
        obj["since"] = datetime.utcnow()
        user = User(**obj)
        user.save()
        return user
    except Exception as e:
        raise e

def update(obj):
    """Update user - equivalent to Node.js update() function"""
    try:
        user = User.objects.get(user_id=obj['user_id'])
        
        # Update fields only if they are provided and not null/false
        if obj.get('email') is not None and obj.get('email') is not False:
            user.email = obj['email']
        
        if obj.get('password') is not None and obj.get('password') is not False:
            user.password = obj['password']
        
        if obj.get('name') is not None and obj.get('name') is not False:
            user.name = obj['name']
        
        if obj.get('role_id') is not None and obj.get('role_id') is not False:
            # Convert role_id string to Role object
            if obj['role_id']:
                try:
                    role = Role.objects.get(id=obj['role_id'])
                    user.role_id = role
                except Role.DoesNotExist:
                    # If role not found, set to None
                    user.role_id = None
            else:
                user.role_id = None
        
        if obj.get('address') is not None and obj.get('address') is not False:
            user.address = obj['address']
        
        if obj.get('status') is not None and obj.get('status') is not False:
            user.status = obj['status']
        
        if obj.get('phone') is not None and obj.get('phone') is not False:
            user.phone = obj['phone']
        
        if obj.get('student_id') is not None and obj.get('student_id') is not False:
            user.student_id = obj['student_id']
        
        user.since = datetime.utcnow()
        user.save()
        return user
    except Exception as e:
        raise e

def find_user(user_id):
    """Find user by ID - equivalent to Node.js find_user() function"""
    try:
        user = User.objects.get(user_id=user_id)
        return user
    except User.DoesNotExist:
        raise Exception("User not found")
    except Exception as e:
        raise e

def find_user_email(email):
    """Find user by email - equivalent to Node.js find_user_email() function"""
    try:
        user = User.objects.get(email=email)
        return user
    except User.DoesNotExist:
        raise Exception("User not found")
    except Exception as e:
        raise e

def remove_user(user_id):
    """Remove user - equivalent to Node.js remove_user() function"""
    try:
        user = User.objects.get(user_id=user_id)
        user.delete()
        return {"deleted": True, "user_id": user_id}
    except User.DoesNotExist:
        raise Exception("User not found")
    except Exception as e:
        raise e
