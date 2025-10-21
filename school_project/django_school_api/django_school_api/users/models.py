from mongoengine import Document, fields
from datetime import datetime
import uuid

class Role(Document):
    name = fields.StringField(max_length=255)
    since = fields.DateTimeField(default=datetime.utcnow)
    
    meta = {
        'collection': 'roles',
        'ordering': ['-since']
    }
    
    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        if not self.since:
            self.since = datetime.utcnow()
        super().save(*args, **kwargs)

class Class(Document):
    name = fields.StringField(max_length=255)
    since = fields.DateTimeField(default=datetime.utcnow)
    
    meta = {
        'collection': 'classes',
        'ordering': ['-since']
    }
    
    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        if not self.since:
            self.since = datetime.utcnow()
        super().save(*args, **kwargs)

class User(Document):
    user_id = fields.IntField(primary_key=True)
    email = fields.EmailField(required=True, unique=True)
    password = fields.StringField(max_length=255)
    name = fields.StringField(max_length=255)
    role_id = fields.ReferenceField(Role)
    address = fields.StringField()
    status = fields.BooleanField(default=True)
    phone = fields.StringField(max_length=20)
    student_id = fields.StringField(max_length=50)
    since = fields.DateTimeField(default=datetime.utcnow)
    
    meta = {
        'collection': 'users',
        'ordering': ['-since']
    }
    
    def __str__(self):
        return f"{self.name} ({self.email})"
    
    def save(self, *args, **kwargs):
        if not self.user_id:
            # Auto-increment user_id
            last_user = User.objects.order_by('-user_id').first()
            self.user_id = (last_user.user_id + 1) if last_user and last_user.user_id else 1
        if not self.since:
            self.since = datetime.utcnow()
        super().save(*args, **kwargs)

class Attendance(Document):
    user = fields.ReferenceField(User)
    approve_by = fields.ReferenceField(User)
    class_obj = fields.ReferenceField(Class)
    checkIn_time = fields.DateTimeField()
    checkOut_time = fields.DateTimeField()
    since = fields.DateTimeField(default=datetime.utcnow)
    
    meta = {
        'collection': 'attendances',
        'ordering': ['-since']
    }
    
    def __str__(self):
        return f"{self.user.name if self.user else 'Unknown'} - {self.class_obj.name if self.class_obj else 'Unknown Class'}"
    
    def save(self, *args, **kwargs):
        if not self.since:
            self.since = datetime.utcnow()
        super().save(*args, **kwargs)

class Notice(Document):
    title = fields.StringField(max_length=255)
    content = fields.StringField()
    status = fields.BooleanField(default=True)
    since = fields.DateTimeField(default=datetime.utcnow)
    
    meta = {
        'collection': 'notices',
        'ordering': ['-since']
    }
    
    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        if not self.since:
            self.since = datetime.utcnow()
        super().save(*args, **kwargs)
