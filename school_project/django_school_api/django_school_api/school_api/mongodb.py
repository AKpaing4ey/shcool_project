"""
MongoDB connection setup for MongoEngine
"""
from mongoengine import connect
from django.conf import settings

def connect_to_mongodb():
    """Connect to MongoDB using MongoEngine"""
    try:
        connect(
            host=settings.MONGODB_SETTINGS['host'],
            connect=settings.MONGODB_SETTINGS['connect']
        )
        print("Connected to MongoDB successfully")
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
