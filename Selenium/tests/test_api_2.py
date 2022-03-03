import requests


class TestApi2:
    """Check to correct work of app"""

    def test_app_is_available(self):
        response = requests.get("https://petstore.swagger.io/")
        assert response.ok

    def test_new_pet(self, adding_pet):
        """Test add new pet"""
        response = adding_pet
        assert response.status_code == 200

    def test_check_adding(self):
        """Test check that pet is add"""
        response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=available")
        assert response.status_code == 200

    def test_update_name(self, update_name_pet):
        """Test update name of pet"""
        response = update_name_pet
        assert response.status_code == 200

    def test_check_updating(self):
        """Test check that the name of pet is update"""
        response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=available")
        assert response.status_code == 200
