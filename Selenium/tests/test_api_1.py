import requests
import time

from Selenium.sources.variables import api_url


class TestApi_1:

    @classmethod
    def setup(cls):
        cls.username = "some_very_strange_username"

    def test_api_user(self):
        response = requests.post(api_url + "/user", json={
          "id": 0,
          "username": self.username,
          "firstName": "string",
          "lastName": "string",
          "email": "string@string",
          "password": "string",
          "phone": "string",
          "userStatus": 1
        },
        headers={
            "accept": "application/json",
            "Content-Type": "application/json"
        })
        assert response.status_code == 200

    def test_api_user_login(self):
        time.sleep(20)
        assert requests.get(api_url + "/user/login", params={"username": self.username, "password": "string"}).status_code == 200

    def test_api_user_get(self):
        time.sleep(120)
        assert requests.get(api_url + f'/user/{self.username}').status_code == 200

    def test_api_user_logout(self):
        assert requests.get(api_url + "/user/logout").status_code == 200
        time.sleep(20)

    def test_api_user_delete(self):
        assert requests.delete(api_url + f'/user/{self.username}').status_code == 200