import re
from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if self._user_repository.find_by_username(username):
            raise UserInputError(f"Username '{username}' is already taken")

        if not self.is_valid_username(username):
            raise UserInputError(f"Username must be at least 3 characters long, and contain letters a-z")

        if not self.is_valid_password(password):
            raise UserInputError(f"Password must be at least 8 characters long, and contain special characters")

    def is_valid_username(self, username):
        if len(username) < 3:
            return False
        if not re.search("^[a-z]+$", username):
            return False
        return True

    def is_valid_password(self, password):
        if len(password) < 8:
            return False
        if re.search("[^a-z]", password):
            return True
        else:
            return False