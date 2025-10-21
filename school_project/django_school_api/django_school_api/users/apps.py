from django.apps import AppConfig
from school_api.mongodb import connect_to_mongodb

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    
    def ready(self):
        # Connect to MongoDB when the app is ready
        connect_to_mongodb()
