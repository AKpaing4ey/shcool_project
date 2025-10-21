# Django School API - MongoDB Microservice

A Django REST API microservice equivalent to the Node.js school management system, built with Django REST Framework and MongoDB.

## Features

- **User Management**: Complete CRUD operations for users
- **JWT Authentication**: Secure token-based authentication
- **MongoDB Integration**: Using Djongo for MongoDB connectivity
- **Pagination**: Built-in pagination for user listings
- **Auto-increment IDs**: Automatic user ID generation
- **CORS Support**: Cross-origin resource sharing enabled
- **RESTful API**: Clean REST API endpoints

## Project Structure

```
django_school_api/
├── manage.py
├── requirements.txt
├── .env.example
├── README.md
├── school_api/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── users/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── urls.py
    ├── views.py
    ├── jwt_utils.py
    └── authentication/
        ├── __init__.py
        └── jwt_auth.py
```

## Prerequisites

- Python 3.8+
- MongoDB 4.0+
- pip (Python package installer)

## Installation & Setup

### 1. Clone or Download the Project

```bash
# If you have the project files, navigate to the directory
cd django_school_api
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

```bash
# Copy the example environment file
cp .env.example .env

# Edit the .env file with your configuration
# SECRET_KEY=your-secret-key-here
# DEBUG=True
# JWT_SECRET_KEY=your-jwt-secret-key-here
```

### 5. MongoDB Setup

Make sure MongoDB is running on your system:

```bash
# Start MongoDB service
# On macOS with Homebrew:
brew services start mongodb-community

# On Ubuntu/Debian:
sudo systemctl start mongod

# On Windows:
# Start MongoDB service from Services or run mongod.exe
```

### 6. Database Migration

```bash
# Create and apply migrations
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

### Authentication

- **POST** `/api/v1/login/` - Login and get JWT token

### User Management

- **GET** `/api/v1/users/` - Get all users (paginated)
- **POST** `/api/v1/users/create/` - Create a new user
- **GET** `/api/v1/users/{user_id}/` - Get user by ID
- **PUT** `/api/v1/users/{user_id}/update/` - Update user
- **DELETE** `/api/v1/users/{user_id}/delete/` - Delete user
- **GET** `/api/v1/users/email/{email}/` - Get user by email

## API Usage Examples

### 1. Create a User

```bash
curl -X POST http://127.0.0.1:8000/api/v1/users/create/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "password123",
    "name": "John Doe",
    "address": "123 Main St",
    "phone": "555-1234",
    "student_id": "STU001",
    "status": true
  }'
```

### 2. Login

```bash
curl -X POST http://127.0.0.1:8000/api/v1/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "password123"
  }'
```

### 3. Get All Users (with JWT token)

```bash
curl -X GET http://127.0.0.1:8000/api/v1/users/ \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

### 4. Update User

```bash
curl -X PUT http://127.0.0.1:8000/api/v1/users/1/update/ \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Smith",
    "phone": "555-5678"
  }'
```

### 5. Delete User

```bash
curl -X DELETE http://127.0.0.1:8000/api/v1/users/1/delete/ \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

## Database Schema

### User Model

```python
{
    "user_id": "Auto-increment primary key",
    "email": "Unique email address",
    "password": "User password",
    "name": "User's full name",
    "address": "User's address",
    "status": "Boolean status (active/inactive)",
    "phone": "Phone number",
    "student_id": "Student identification number",
    "since": "Registration date (auto-generated)"
}
```

## Key Differences from Node.js Version

1. **Framework**: Django REST Framework instead of Express.js
2. **ORM**: Django ORM with Djongo instead of Mongoose
3. **Authentication**: Custom JWT authentication class
4. **Serialization**: Django REST Framework serializers
5. **Pagination**: Built-in pagination support
6. **Admin Interface**: Django admin for data management

## Development

### Running Tests

```bash
python manage.py test
```

### Django Admin

Access the admin interface at `http://127.0.0.1:8000/admin/` after creating a superuser.

### API Documentation

The API follows RESTful conventions and includes proper HTTP status codes:

- `200 OK` - Successful GET/PUT requests
- `201 Created` - Successful POST requests
- `204 No Content` - Successful DELETE requests
- `400 Bad Request` - Invalid request data
- `401 Unauthorized` - Authentication required
- `404 Not Found` - Resource not found

## Production Deployment

For production deployment:

1. Set `DEBUG=False` in settings
2. Use a proper database (MongoDB Atlas)
3. Set secure `SECRET_KEY` and `JWT_SECRET_KEY`
4. Configure proper CORS settings
5. Use a production WSGI server (Gunicorn)
6. Set up proper logging

## Troubleshooting

### Common Issues

1. **MongoDB Connection Error**: Ensure MongoDB is running and accessible
2. **Import Errors**: Make sure all dependencies are installed in the virtual environment
3. **JWT Token Issues**: Check JWT_SECRET_KEY configuration
4. **CORS Issues**: Verify CORS settings in settings.py

### Logs

Check Django logs for detailed error information:

```bash
python manage.py runserver --verbosity=2
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the MIT License.
