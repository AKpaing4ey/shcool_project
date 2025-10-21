# User and Role Creation Guide

This guide provides commands for creating roles and users in the Django School API using MongoEngine.

## Prerequisites

- Django server must be running
- Virtual environment must be activated
- MongoDB connection must be established

## Commands

### 1. Create a New Role

```bash
cd /Users/nandakyawwin/Desktop/django_school_api/django_school_api
source venv/bin/activate
python manage.py shell -c "
from users.models import Role
from datetime import datetime

# Create a new role
new_role = Role(name='role_name')
new_role.save()
print(f'Created role: {new_role.name} (ID: {new_role.id})')
"
```

**Example - Create Admin Role:**
```bash
python manage.py shell -c "
from users.models import Role
admin_role = Role(name='admin')
admin_role.save()
print(f'Created role: {admin_role.name} (ID: {admin_role.id})')
"
```

### 2. Create a User with Specific Role

```bash
python manage.py shell -c "
from users.models import Role, User
from datetime import datetime

# Get the role (replace 'role_name' with actual role name)
role = Role.objects(name='role_name').first()

# Create user with role
new_user = User(
    email='user@example.com',
    password='password123',
    name='User Name',
    role_id=role,
    address='User Address',
    phone='123-456-7890',
    student_id='STU001'
)
new_user.save()
print(f'Created user: {new_user.name} ({new_user.email}) with role: {new_user.role_id.name}')
print(f'User ID: {new_user.user_id}')
"
```

### 3. Create Role and User in One Command

```bash
python manage.py shell -c "
from users.models import Role, User
from datetime import datetime

# Create role first
admin_role = Role(name='admin')
admin_role.save()
print(f'Created role: {admin_role.name} (ID: {admin_role.id})')

# Create user with the role
new_user = User(
    email='admin_user@example.com',
    password='admin123',
    name='Admin User',
    role_id=admin_role,
    address='123 Admin Street',
    phone='123-456-7890',
    student_id='ADM001'
)
new_user.save()
print(f'Created user: {new_user.name} ({new_user.email}) with role: {new_user.role_id.name}')
print(f'User ID: {new_user.user_id}')
"
```

## Field Descriptions

### Role Fields
- `name` (StringField): Name of the role (e.g., 'admin', 'teacher', 'student')
- `since` (DateTimeField): Creation timestamp (auto-generated)

### User Fields
- `user_id` (IntField): Auto-incrementing primary key
- `email` (EmailField): User's email address (required, unique)
- `password` (StringField): User's password
- `name` (StringField): User's full name
- `role_id` (ReferenceField): Reference to Role document
- `address` (StringField): User's address
- `status` (BooleanField): User status (default: True)
- `phone` (StringField): User's phone number
- `student_id` (StringField): Student/employee ID
- `since` (DateTimeField): Creation timestamp (auto-generated)

## Example Outputs

### Successful Role Creation
```
Connected to MongoDB successfully
Created role: admin (ID: 68f0ea6bf7b44fbc35dcc79f)
```

### Successful User Creation
```
Connected to MongoDB successfully
Created role: admin (ID: 68f0ea6bf7b44fbc35dcc79f)
Created user: Admin User (admin_user@example.com) with role: admin
User ID: 2
```

## Common Role Types

- `admin` - Administrative access
- `teacher` - Teacher privileges
- `student` - Student access
- `staff` - Staff member
- `parent` - Parent/guardian access

## Notes

- User IDs are auto-incrementing starting from 1
- All timestamps are automatically set to current UTC time
- Email addresses must be unique across all users
- Passwords should be hashed before saving in production
- Role names are case-sensitive

## Troubleshooting

### Role Not Found Error
If you get a "Role not found" error, make sure the role exists first:
```bash
python manage.py shell -c "
from users.models import Role
roles = Role.objects()
for role in roles:
    print(f'Role: {role.name} (ID: {role.id})')
"
```

### Duplicate Email Error
If you get a duplicate email error, use a different email address or check existing users:
```bash
python manage.py shell -c "
from users.models import User
users = User.objects()
for user in users:
    print(f'User: {user.name} ({user.email})')
"
```
