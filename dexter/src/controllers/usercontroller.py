import hashlib
import binascii
import os
from src.models import Users
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

def hash_password(password, salt):
    """
    Create a hashed password using provided password and salt.

    Args:
        password (str): The password string to be hashed.
        salt (str): The salt to be used for hashing the password.

    Returns:
        str: The hashed password.
    """
    pwdhash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('ascii'), 100000)
    return binascii.hexlify(pwdhash).decode('ascii')

class UserController:
    """
    Controller for handling user related operations.
    """

    def get_user(self, email):
        """
        Get a user object by the given email.

        Args:
            email (str): The email of the user.

        Returns:
            Users: A user object if found. None otherwise.
        """
        try:
            return Users.objects.get(email=email)
        except ObjectDoesNotExist:
            return None

    def add_user(self, email, password, salt):
        """
        Create a new user with the given email, password and salt.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.
            salt (str): The salt for hashing the password.

        Returns:
            Users: The created user object.
        """
        hashed_password = hash_password(password, salt)
        return Users.objects.create(email=email, password=hashed_password, salt=salt, is_active=1)

    def login(self, email, password):
        """
        Validate the login information provided by the user.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            dict: Dictionary containing refresh and access tokens if user validation is successful. None otherwise.
        """
        user = self.get_user(email)
        if user is None:
            raise ValidationError("user does not exits")

        hashed_password = hash_password(password, user.salt)
        if hashed_password != user.password:
            raise ValidationError("invalid password")

        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def signup(self, email, password):
        """
        Sign up a new user.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            str: A success message if user signup is successful. None otherwise.
        """
        salt = binascii.hexlify(os.urandom(8)).decode('ascii')
        if self.get_user(email) is not None:
            raise ValidationError("User Already Exits")

        self.add_user(email, password, salt)
        return "User Created"
