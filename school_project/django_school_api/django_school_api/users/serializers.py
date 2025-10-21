from rest_framework import serializers
from .models import User, Role, Class, Attendance, Notice

class UserSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255, write_only=True)
    name = serializers.CharField(max_length=255)
    role_id = serializers.CharField(required=False, allow_blank=True)
    address = serializers.CharField(required=False, allow_blank=True)
    status = serializers.BooleanField(default=True)
    phone = serializers.CharField(max_length=20, required=False, allow_blank=True)
    student_id = serializers.CharField(max_length=50, required=False, allow_blank=True)
    since = serializers.DateTimeField(read_only=True)

class UserWithRoleSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255, write_only=True)
    name = serializers.CharField(max_length=255)
    role = serializers.SerializerMethodField()
    address = serializers.CharField(required=False, allow_blank=True)
    status = serializers.BooleanField(default=True)
    phone = serializers.CharField(max_length=20, required=False, allow_blank=True)
    student_id = serializers.CharField(max_length=50, required=False, allow_blank=True)
    since = serializers.DateTimeField(read_only=True)

    def get_role(self, obj):
        if obj.role_id:
            return {
                'id': str(obj.role_id.id),
                'name': obj.role_id.name,
                'since': obj.role_id.since.isoformat() if obj.role_id.since else None
            }
        return None

    def create(self, validated_data):
        # Handle role_id separately
        if 'role_id' in validated_data:
            role_id = validated_data.pop('role_id')
            if role_id:
                try:
                    role = Role.objects.get(id=role_id)
                    validated_data['role_id'] = role
                except Role.DoesNotExist:
                    pass
        
        user = User(**validated_data)
        user.save()
        return user

    def update(self, instance, validated_data):
        # Handle role_id separately
        if 'role_id' in validated_data:
            role_id = validated_data.pop('role_id')
            if role_id:
                try:
                    role = Role.objects.get(id=role_id)
                    instance.role_id = role
                except Role.DoesNotExist:
                    pass
        
        # Only update fields that are provided and not None/False
        for field, value in validated_data.items():
            if value is not None and value is not False:
                setattr(instance, field, value)
        instance.save()
        return instance

class UserCreateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    role_id = serializers.CharField(required=False, allow_blank=True)
    address = serializers.CharField(required=False, allow_blank=True)
    status = serializers.BooleanField(default=True)
    phone = serializers.CharField(max_length=20, required=False, allow_blank=True)
    student_id = serializers.CharField(max_length=50, required=False, allow_blank=True)

    def create(self, validated_data):
        # Handle role_id separately
        if 'role_id' in validated_data:
            role_id = validated_data.pop('role_id')
            if role_id:
                try:
                    role = Role.objects.get(id=role_id)
                    validated_data['role_id'] = role
                except Role.DoesNotExist:
                    pass
        
        user = User(**validated_data)
        user.save()
        return user

class UserUpdateSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    password = serializers.CharField(max_length=255, required=False)
    name = serializers.CharField(max_length=255, required=False)
    role_id = serializers.CharField(required=False, allow_blank=True)
    address = serializers.CharField(required=False, allow_blank=True)
    status = serializers.BooleanField(required=False)
    phone = serializers.CharField(max_length=20, required=False, allow_blank=True)
    student_id = serializers.CharField(max_length=50, required=False, allow_blank=True)

    def update(self, instance, validated_data):
        # Handle role_id separately
        if 'role_id' in validated_data:
            role_id = validated_data.pop('role_id')
            if role_id:
                try:
                    role = Role.objects.get(id=role_id)
                    instance.role_id = role
                except Role.DoesNotExist:
                    pass
        
        # Only update fields that are provided and not None/False
        for field, value in validated_data.items():
            if value is not None and value is not False:
                setattr(instance, field, value)
        instance.save()
        return instance

# Role Serializers
class RoleSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=255)
    since = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        role = Role(**validated_data)
        role.save()
        return role

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance

class RoleCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        role = Role(**validated_data)
        role.save()
        return role

# Class Serializers
class ClassSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=255)
    since = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        class_obj = Class(**validated_data)
        class_obj.save()
        return class_obj

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance

class ClassCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        class_obj = Class(**validated_data)
        class_obj.save()
        return class_obj

# Attendance Serializers
class AttendanceSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user = serializers.CharField()
    approve_by = serializers.CharField(required=False, allow_blank=True)
    class_obj = serializers.CharField()
    checkIn_time = serializers.DateTimeField(required=False)
    checkOut_time = serializers.DateTimeField(required=False)
    since = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        # Handle user reference
        user_id = validated_data.pop('user')
        try:
            user = User.objects.get(user_id=user_id)
            validated_data['user'] = user
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found")
        
        # Handle approve_by reference
        if 'approve_by' in validated_data and validated_data['approve_by']:
            approve_by_id = validated_data.pop('approve_by')
            try:
                approve_by = User.objects.get(user_id=approve_by_id)
                validated_data['approve_by'] = approve_by
            except User.DoesNotExist:
                pass
        
        # Handle class reference
        class_id = validated_data.pop('class_obj')
        try:
            class_obj = Class.objects.get(id=class_id)
            validated_data['class_obj'] = class_obj
        except Class.DoesNotExist:
            raise serializers.ValidationError("Class not found")
        
        attendance = Attendance(**validated_data)
        attendance.save()
        return attendance

    def update(self, instance, validated_data):
        # Handle user reference
        if 'user' in validated_data:
            user_id = validated_data.pop('user')
            try:
                user = User.objects.get(user_id=user_id)
                validated_data['user'] = user
            except User.DoesNotExist:
                raise serializers.ValidationError("User not found")
        
        # Handle approve_by reference
        if 'approve_by' in validated_data and validated_data['approve_by']:
            approve_by_id = validated_data.pop('approve_by')
            try:
                approve_by = User.objects.get(user_id=approve_by_id)
                validated_data['approve_by'] = approve_by
            except User.DoesNotExist:
                pass
        
        # Handle class reference
        if 'class_obj' in validated_data:
            class_id = validated_data.pop('class_obj')
            try:
                class_obj = Class.objects.get(id=class_id)
                validated_data['class_obj'] = class_obj
            except Class.DoesNotExist:
                raise serializers.ValidationError("Class not found")
        
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance

class AttendanceCreateSerializer(serializers.Serializer):
    user = serializers.CharField()
    approve_by = serializers.CharField(required=False, allow_blank=True)
    class_obj = serializers.CharField()
    checkIn_time = serializers.DateTimeField(required=False)
    checkOut_time = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        # Handle user reference
        user_id = validated_data.pop('user')
        try:
            user = User.objects.get(user_id=user_id)
            validated_data['user'] = user
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found")
        
        # Handle approve_by reference
        if 'approve_by' in validated_data and validated_data['approve_by']:
            approve_by_id = validated_data.pop('approve_by')
            try:
                approve_by = User.objects.get(user_id=approve_by_id)
                validated_data['approve_by'] = approve_by
            except User.DoesNotExist:
                pass
        
        # Handle class reference
        class_id = validated_data.pop('class_obj')
        try:
            class_obj = Class.objects.get(id=class_id)
            validated_data['class_obj'] = class_obj
        except Class.DoesNotExist:
            raise serializers.ValidationError("Class not found")
        
        attendance = Attendance(**validated_data)
        attendance.save()
        return attendance

# Notice Serializers
class NoticeSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    status = serializers.BooleanField(default=True)
    since = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        notice = Notice(**validated_data)
        notice.save()
        return notice

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance

class NoticeCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    status = serializers.BooleanField(default=True)

    def create(self, validated_data):
        notice = Notice(**validated_data)
        notice.save()
        return notice
