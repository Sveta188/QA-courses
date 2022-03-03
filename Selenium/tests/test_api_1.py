import requests
import time

from Selenium.sources.variables import api_url


class TestApi_1:

    @classmethod
    def setup(cls):
        cls.username = "string"

    def test_api_user(self):
        response = requests.post(api_url + "/user", json={
          "id": 0,
          "username": self.username,
          "firstName": "string",
          "lastName": "string",
          "email": "string",
          "password": "string",
          "phone": "string",
          "userStatus": 0
        },
        headers={
            "accept": "application/json",
            "Content-Type": "application/json"
        })
        assert response.status_code == 200

    def test_api_user_login(self):
        assert requests.get(api_url + "/user/login", params={"username": self.username, "password": "string"}).status_code == 200

    def test_api_user_get(self):
        assert requests.get(api_url + f'/user/{self.username}').status_code == 200

    def test_api_user_logout(self):
        assert requests.get(api_url + "/user/logout").status_code == 200

    def test_api_user_delete(self):
        assert requests.delete(api_url + f'/user/{self.username}').status_code == 200