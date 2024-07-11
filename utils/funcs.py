import bcrypt
from api.models import User

def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password

def verify_password(stored_password, provided_password):
    # Verify the provided password against the stored password
    return bcrypt.checkpw(provided_password.encode(), stored_password)

def strip_sc(input_str):
    # Define a set of allowed characters (alphanumeric and space)
    allowed_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
    # Filter out characters that are not in the allowed set
    cleaned_str = ''.join(char for char in input_str if char in allowed_characters)
    return cleaned_str


def authenticate(email, password):
    return User.objects.filter(email=email, password=password)
