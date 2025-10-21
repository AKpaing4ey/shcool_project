#!/bin/bash

# Django School API - Payload Testing Script
# This script demonstrates all the create and update payloads for the admin routes

BASE_URL="http://localhost:8001/admin/api/v_1"

echo "🚀 Testing Django School API Admin Routes Payloads"
echo "=================================================="

# Test Role Creation
echo "📝 Testing Role Creation..."
curl -X POST $BASE_URL/role/create/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Role"}' \
  -w "\nStatus: %{http_code}\n\n"

# Test Notice Creation
echo "📝 Testing Notice Creation..."
curl -X POST $BASE_URL/notice/create/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Test Notice", "content": "This is a test notice", "status": true}' \
  -w "\nStatus: %{http_code}\n\n"

# Test Class Creation
echo "📝 Testing Class Creation..."
curl -X POST $BASE_URL/class/create/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Class"}' \
  -w "\nStatus: %{http_code}\n\n"

# Test User Sign Up
echo "📝 Testing User Sign Up..."
curl -X POST $BASE_URL/user/sign_up/ \
  -H "Content-Type: application/json" \
  -d '{"phone": "+1234567890", "email": "test@school.com", "password": "password123", "name": "Test User", "address": "123 Test Street"}' \
  -w "\nStatus: %{http_code}\n\n"

# Test Attendance Creation
echo "📝 Testing Attendance Creation..."
curl -X POST $BASE_URL/attendance/create/ \
  -H "Content-Type: application/json" \
  -d '{"user": 1, "class_obj": "68ebb3cc7c7a1dba85f8fe6f", "checkIn_time": "2025-10-12T08:00:00", "checkOut_time": "2025-10-12T10:00:00"}' \
  -w "\nStatus: %{http_code}\n\n"

echo "✅ All payload tests completed!"
echo "📋 Check the responses above for success/error status"
echo "📖 For detailed payload documentation, see API_PAYLOADS.md"
echo "🔧 For JSON examples, see example_payloads.json"

echo ""
echo "🗑️  Testing Delete Operations..."
echo "================================="

# Test Role Delete
echo "🗑️  Testing Role Delete..."
curl -X POST $BASE_URL/role/delete/ \
  -H "Content-Type: application/json" \
  -d '{"id": "68ebb0dd69562c09046fbc62"}' \
  -w "\nStatus: %{http_code}\n\n"

# Test Notice Delete
echo "🗑️  Testing Notice Delete..."
curl -X POST $BASE_URL/notice/delete/ \
  -H "Content-Type: application/json" \
  -d '{"id": "68ebb259f134573e945cca72"}' \
  -w "\nStatus: %{http_code}\n\n"

# Test Class Delete
echo "🗑️  Testing Class Delete..."
curl -X POST $BASE_URL/class/delete/ \
  -H "Content-Type: application/json" \
  -d '{"class_id": "68eb475f196f800c4f0f0c1a"}' \
  -w "\nStatus: %{http_code}\n\n"

# Test User Delete
echo "🗑️  Testing User Delete..."
curl -X POST $BASE_URL/user/delete/ \
  -H "Content-Type: application/json" \
  -d '{"user_id": 3}' \
  -w "\nStatus: %{http_code}\n\n"

echo "✅ All delete tests completed!"
echo "📝 Note: User deletion uses 'user_id' (integer), others use 'id' or 'class_id' (MongoDB ObjectId strings)"
