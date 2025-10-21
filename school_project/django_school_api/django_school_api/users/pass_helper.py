"""
Password hashing helper - equivalent to Node.js bcrypt helper
"""
import hashlib
import secrets

def encrypt(password):
    """Encrypt password - equivalent to Node.js bcrypt.encrypt()"""
    # Using SHA-256 with salt for simplicity (in production, use bcrypt)
    salt = secrets.token_hex(16)
    password_hash = hashlib.sha256((password + salt).encode()).hexdigest()
    return f"{salt}:{password_hash}"

def compare(password, hashed_password):
    """Compare password - equivalent to Node.js bcrypt.compare()"""
    try:
        salt, stored_hash = hashed_password.split(':')
        password_hash = hashlib.sha256((password + salt).encode()).hexdigest()
        return password_hash == stored_hash
    except:
        return False
