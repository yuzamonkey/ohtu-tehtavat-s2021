import requests


class PlayerReader:
    def __init__(self, url):
        self._response = requests.get(url).json()

    def get_response(self):
        return self._response
