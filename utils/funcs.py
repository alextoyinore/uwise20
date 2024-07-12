import bcrypt
from api.models import User
from django.contrib.auth.hashers import check_password


def hash_it(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password


def verify_hash(stored_password, provided_password):
    # Verify the provided password against the stored password
    return bcrypt.checkpw(provided_password.encode(), stored_password)


def strip_sc(input_str):
    # Define a set of allowed characters (alphanumeric and space)
    allowed_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
    # Filter out characters that are not in the allowed set
    cleaned_str = ''.join(char for char in input_str if char in allowed_characters)
    return cleaned_str


def authenticate_user(email, password):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None

    if check_password(password, user.password):
        return user
    return None
