# Django School API - Admin Routes Payloads

This document contains all the payload structures for create and update operations across all admin routes.

## Base URL
```
http://localhost:8001/admin/api/v_1/
```

---

## User Routes

### Sign Up (Create User)
**POST** `/admin/api/v_1/user/sign_up/`

```json
{
  "phone": "+1234567890",
  "email": "john.student@school.com",
  "password": "password123",
  "role_id": "68eb4750196f800c4f0f0c18",
  "name": "John Student",
  "address": "123 Student Street"
}
```

### Update User
**PUT** `/admin/api/v_1/user/update/`

```json
{
  "user_id": 1,
  "phone": "+1234567890",
  "email": "john.student@school.com",
  "password": "newpassword123",
  "role_id": "68eb4753196f800c4f0f0c19",
  "name": "John Updated Student",
  "address": "456 Updated Street",
  "status": true,
  "student_id": "STU002"
}
```

**Note:** All fields are optional except `user_id`. Only include fields you want to update. The `role_id` should be a valid MongoDB ObjectId string.

### Delete User
**POST** `/admin/api/v_1/user/delete/`

```json
{
  "user_id": 1
}
```

**Note**: For user deletion, use `user_id` (integer) instead of MongoDB ObjectId.

---

## Role Routes

### Create Role
**POST** `/admin/api/v_1/role/create/`

```json
{
  "name": "Principal"
}
```

### Update Role
**PUT** `/admin/api/v_1/role/update/`

```json
{
  "id": "68ebb23bf134573e945cca71",
  "name": "Updated Principal"
}
```

### Delete Role
**POST** `/admin/api/v_1/role/delete/`

```json
{
  "id": "68ebb23bf134573e945cca71"
}
```

---

## Notice Routes

### Create Notice
**POST** `/admin/api/v_1/notice/create/`

```json
{
  "title": "School Holiday Notice",
  "content": "School will be closed on Monday for holiday.",
  "status": true
}
```

### Update Notice
**PUT** `/admin/api/v_1/notice/update/`

```json
{
  "id": "68eb4767196f800c4f0f0c1b",
  "title": "Updated Holiday Notice",
  "content": "School will be closed on Monday and Tuesday for holiday.",
  "status": false
}
```

### Delete Notice
**POST** `/admin/api/v_1/notice/delete/`

```json
{
  "id": "68eb4767196f800c4f0f0c1b"
}
```

---

## Class Routes

### Create Class
**POST** `/admin/api/v_1/class/create/`

```json
{
  "name": "Mathematics"
}
```

### Update Class
**PUT** `/admin/api/v_1/class/update/`

```json
{
  "id": "68eb475f196f800c4f0f0c1a",
  "name": "Advanced Mathematics"
}
```

### Delete Class
**POST** `/admin/api/v_1/class/delete/`

```json
{
  "class_id": "68eb475f196f800c4f0f0c1a"
}
```

---

## Attendance Routes

### Create Attendance
**POST** `/admin/api/v_1/attendance/create/`

```json
{
  "user": 1,
  "approve_by": 2,
  "class_obj": "68eb475f196f800c4f0f0c1a",
  "checkIn_time": "2025-10-12T08:00:00",
  "checkOut_time": "2025-10-12T10:00:00"
}
```

### Update Attendance
**PUT** `/admin/api/v_1/attendance/update/`

```json
{
  "id": "68eb476a196f800c4f0f0c1c",
  "user": 1,
  "approve_by": 2,
  "class_obj": "68eb475f196f800c4f0f0c1a",
  "checkIn_time": "2025-10-12T08:30:00",
  "checkOut_time": "2025-10-12T11:00:00"
}
```

### Delete Attendance
**POST** `/admin/api/v_1/attendance/delete/`

```json
{
  "id": "68eb476a196f800c4f0f0c1c"
}
```

### Delete Role
**POST** `/admin/api/v_1/role/delete/`

```json
{
  "id": "68ebb23bf134573e945cca71"
}
```

### Delete Notice
**POST** `/admin/api/v_1/notice/delete/`

```json
{
  "id": "68eb4767196f800c4f0f0c1b"
}
```

### Delete Class
**POST** `/admin/api/v_1/class/delete/`

```json
{
  "class_id": "68eb475f196f800c4f0f0c1a"
}
```

### Delete Attendance
**POST** `/admin/api/v_1/attendance/delete/`

```json
{
  "id": "68eb476a196f800c4f0f0c1c"
}
```

---

## Authentication Routes

### Sign In
**POST** `/admin/api/v_1/user/sign_in/`

```json
{
  "email": "john.student@school.com",
  "password": "password123"
}
```

---

## Delete Operations Summary

All delete operations use **POST** method with the following patterns:

### User Delete
- **Field**: `user_id` (integer)
- **Example**: `{"user_id": 1}`

### Role Delete  
- **Field**: `id` (MongoDB ObjectId string)
- **Example**: `{"id": "68ebb23bf134573e945cca71"}`

### Notice Delete
- **Field**: `id` (MongoDB ObjectId string)
- **Example**: `{"id": "68eb4767196f800c4f0f0c1b"}`

### Class Delete
- **Field**: `class_id` (MongoDB ObjectId string)
- **Example**: `{"class_id": "68eb475f196f800c4f0f0c1a"}`

### Attendance Delete
- **Field**: `id` (MongoDB ObjectId string)
- **Example**: `{"id": "68eb476a196f800c4f0f0c1c"}`

**Important Notes:**
- User deletion uses `user_id` (integer) - this is different from other models
- All other models use `id` or `class_id` (MongoDB ObjectId strings)
- Delete operations return success confirmation with the deleted ID
- Failed deletions return appropriate error messages

---

## Field Descriptions

### User Fields
- `user_id` (integer): Auto-incremented user ID
- `phone` (string): User's phone number
- `email` (string): User's email address (unique)
- `password` (string): User's password (hashed)
- `role_id` (string): MongoDB ObjectId of the role
- `name` (string): User's full name
- `address` (string): User's address
- `status` (boolean): User's active status
- `student_id` (string): Student ID (optional)
- `since` (datetime): Creation timestamp (auto-generated)

### Role Fields
- `id` (string): MongoDB ObjectId
- `name` (string): Role name
- `since` (datetime): Creation timestamp (auto-generated)

### Notice Fields
- `id` (string): MongoDB ObjectId
- `title` (string): Notice title
- `content` (string): Notice content
- `status` (boolean): Notice active status
- `since` (datetime): Creation timestamp (auto-generated)

### Class Fields
- `id` (string): MongoDB ObjectId
- `name` (string): Class name
- `since` (datetime): Creation timestamp (auto-generated)

### Attendance Fields
- `id` (string): MongoDB ObjectId
- `user` (integer): User ID (user_id from User model)
- `approve_by` (integer): Approver's user ID (optional)
- `class_obj` (string): MongoDB ObjectId of the class
- `checkIn_time` (datetime): Check-in timestamp
- `checkOut_time` (datetime): Check-out timestamp
- `since` (datetime): Creation timestamp (auto-generated)

---

## Response Format

All routes return responses in the following format:

### Success Response
```json
{
  "con": true,
  "data": {
    // Object data or array of objects
  },
  "message": "Success",
  "status": 200,
  "length": 1
}
```

### Error Response
```json
{
  "con": false,
  "data": "Error message",
  "message": "Unsuccessful",
  "status": 500,
  "length": 0
}
```

---

## Example cURL Commands

### Create a Role
```bash
curl -X POST http://localhost:8001/admin/api/v_1/role/create/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Principal"}'
```

### Update a Role
```bash
curl -X PUT http://localhost:8001/admin/api/v_1/role/update/ \
  -H "Content-Type: application/json" \
  -d '{"id": "68ebb23bf134573e945cca71", "name": "Updated Principal"}'
```

### Create a Notice
```bash
curl -X POST http://localhost:8001/admin/api/v_1/notice/create/ \
  -H "Content-Type: application/json" \
  -d '{"title": "New Notice", "content": "This is a new notice", "status": true}'
```

### Create an Attendance
```bash
curl -X POST http://localhost:8001/admin/api/v_1/attendance/create/ \
  -H "Content-Type: application/json" \
  -d '{"user": 1, "class_obj": "68eb475f196f800c4f0f0c1a", "checkIn_time": "2025-10-12T08:00:00"}'
```

### Sign Up a User
```bash
curl -X POST http://localhost:8001/admin/api/v_1/user/sign_up/ \
  -H "Content-Type: application/json" \
  -d '{"phone": "+1234567890", "email": "new@school.com", "password": "password123", "name": "New User", "address": "123 Street"}'
```

### Delete a Role
```bash
curl -X POST http://localhost:8001/admin/api/v_1/role/delete/ \
  -H "Content-Type: application/json" \
  -d '{"id": "68ebb23bf134573e945cca71"}'
```

### Delete a Notice
```bash
curl -X POST http://localhost:8001/admin/api/v_1/notice/delete/ \
  -H "Content-Type: application/json" \
  -d '{"id": "68eb4767196f800c4f0f0c1b"}'
```

### Delete a Class
```bash
curl -X POST http://localhost:8001/admin/api/v_1/class/delete/ \
  -H "Content-Type: application/json" \
  -d '{"class_id": "68eb475f196f800c4f0f0c1a"}'
```

### Delete an Attendance
```bash
curl -X POST http://localhost:8001/admin/api/v_1/attendance/delete/ \
  -H "Content-Type: application/json" \
  -d '{"id": "68eb476a196f800c4f0f0c1c"}'
```

### Delete a User
```bash
curl -X POST http://localhost:8001/admin/api/v_1/user/delete/ \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1}'
```

---

## Notes

1. **Required Fields**: All fields marked as required must be included in create operations
2. **Optional Fields**: Fields not marked as required can be omitted
3. **Auto-generated Fields**: Fields like `id`, `since`, `user_id` are auto-generated and should not be included in create operations
4. **Update Operations**: Only include fields you want to update in PUT requests
5. **Delete Operations**: Only include the ID field in delete operations
6. **Date Format**: Use ISO 8601 format for datetime fields (e.g., "2025-10-12T08:00:00")
7. **MongoDB ObjectIds**: Use string format for MongoDB ObjectIds
8. **User IDs**: Use integer format for user_id fields
9. **Datetime Parsing**: The API automatically converts ISO datetime strings to proper datetime objects
10. **Error Handling**: All routes return consistent error responses with helpful messages
