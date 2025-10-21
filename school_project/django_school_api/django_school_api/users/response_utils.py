"""
Utility functions for standardized API responses matching Node.js format
"""
from rest_framework.response import Response
from rest_framework import status

def response(data, success=True):
    """
    Create a response matching Node.js response format
    
    Args:
        data: The data to return
        success (bool): Whether the operation was successful
    
    Returns:
        dict: Response with con, data, message, status, length
    """
    
    # Determine success status and message
    con = success
    status_code = 200 if success else 500
    
    # Set message based on success
    message = "Success" if success else "Unsuccessful"
    
    # Calculate length based on data type
    if data is None:
        length = 0
    elif isinstance(data, list):
        length = len(data)
    elif isinstance(data, dict):
        # For single objects, length is 1
        length = 1
    else:
        # For other data types, length is 1
        length = 1
    
    # Create response data
    response_data = {
        "con": con,
        "data": data,
        "message": message,
        "status": status_code,
        "length": length
    }
    
    return response_data

def create_response(success=True, data=None, message=None, http_status=200):
    """
    Create a standardized API response
    
    Args:
        success (bool): Whether the operation was successful
        data: The data to return (can be list, dict, or single object)
        message (str): Custom message (defaults to "Success" or "Unsuccessful")
        http_status (int): HTTP status code
    
    Returns:
        Response: Standardized response with con, data, message, status, length
    """
    
    # Determine success status and message
    con = success
    status_code = http_status if success else 500
    
    # Set default message if not provided
    if message is None:
        message = "Success" if success else "Unsuccessful"
    
    # Calculate length based on data type
    if data is None:
        length = 0
    elif isinstance(data, list):
        length = len(data)
    elif isinstance(data, dict):
        # For single objects, length is 1
        length = 1
    else:
        # For other data types, length is 1
        length = 1
    
    # Create response data
    response_data = {
        "con": con,
        "data": data,
        "message": message,
        "status": status_code,
        "length": length
    }
    
    return Response(response_data, status=http_status)

def success_response(data=None, message="Success", http_status=200):
    """Create a successful response"""
    return create_response(success=True, data=data, message=message, http_status=http_status)

def error_response(message="Unsuccessful", data=None, http_status=500):
    """Create an error response"""
    return create_response(success=False, data=data, message=message, http_status=http_status)
