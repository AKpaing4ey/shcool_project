#!/usr/bin/env python3
"""
Simple test script for the Django School API
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/v1"

def test_create_user():
    """Test creating a user"""
    print("Testing user creation...")
    
    user_data = {
        "email": "test@example.com",
        "password": "password123",
        "name": "Test User",
        "address": "123 Test St",
        "phone": "555-1234",
        "student_id": "STU001",
        "status": True
    }
    
    response = requests.post(f"{BASE_URL}/users/create/", json=user_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    return response.json()

def test_login():
    """Test login functionality"""
    print("\nTesting login...")
    
    login_data = {
        "email": "test@example.com",
        "password": "password123"
    }
    
    response = requests.post(f"{BASE_URL}/login/", json=login_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    
    if response.status_code == 200:
        return response.json().get('token')
    return None

def test_get_users(token):
    """Test getting all users"""
    print("\nTesting get all users...")
    
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/users/", headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def test_update_user(token, user_id):
    """Test updating a user"""
    print(f"\nTesting update user {user_id}...")
    
    update_data = {
        "name": "Updated Test User",
        "phone": "555-5678"
    }
    
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.put(f"{BASE_URL}/users/{user_id}/update/", 
                          json=update_data, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

def main():
    """Run all tests"""
    print("Starting API tests...")
    
    try:
        # Test user creation
        user = test_create_user()
        user_id = user.get('user_id')
        
        # Test login
        token = test_login()
        
        if token:
            # Test getting users
            test_get_users(token)
            
            # Test updating user
            if user_id:
                test_update_user(token, user_id)
        
        print("\nAll tests completed!")
        
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the API. Make sure the server is running.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
