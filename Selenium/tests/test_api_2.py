import requests
import time

from Selenium.sources.variables import api_url


class TestApi_2:

    @classmethod
    def setup(cls):
        cls.name = "some_very_strange_name"
        cls.changed_name = "another_very_strange_name"

    def test_api_pet(self):
        response = requests.post(api_url + "/pet", json={
                "id": 0,
                "category": {
                    "id": 0,
                    "name": "string"
                },
                "name": self.name,
                "photoUrls": [
                    "string"
                ],
                "tags": [
                    {
                        "id": 0,
                        "name": "string"
                    }
                ],
                "status": "available"

        },
        headers={
            "accept": "application/json",
            "Content-Type": "application/json"
        })
        petId = response.json()['id']
        assert response.status_code == 200
        time.sleep(20)
        assert requests.get(api_url + f'/pet/{petId}').status_code == 200
        time.sleep(10)
        assert requests.post(api_url + f"/pet/{petId}", data={
                "name": self.changed_name,
                "status": "available"

        },
        headers={
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
        }).status_code == 200
        time.sleep(60)
        response = requests.get(api_url + f'/pet/{petId}')
        assert response.status_code == 200
        assert response.json()['name'] == self.changed_name