import requests


class AppLibrary:
    def __init__(self):
        # self._base_url = "http://localhost:5000"
        self._base_url = "http://127.0.0.1:5000"

        self.reset_application()

    def reset_application(self):
        requests.post(f"{self._base_url}/tests/reset")

    def create_user(self, username, password, password_confirmation):
        data = {
            "username": username,
            "password": password,
            "password_confirmation": password_confirmation
        }

        requests.post(f"{self._base_url}/register", data=data)
