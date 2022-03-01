import os
import time
import pytest
import psycopg2
import requests
import uuid

from selenium.webdriver.common.by import By

api_url = os.getenv('REMOTE_API_URL')
dbname=os.getenv('DB_NAME')
user=os.getenv('DB_USER')
password=os.getenv('DB_PASSWORD')
host=os.getenv('DB_HOST')

group_name = os.getenv('GROUP_NAME')
user_name = os.getenv('USER_NAME')
user_password = os.getenv('USER_PASSWORD')


@pytest.mark.usefixtures('db_1')
class Test_group_1:

    @classmethod
    def setup(cls):
        cls.username = "some_very_strange_username"

    def test_group(self, login_fixture):
        login_fixture.find_element(By.CSS_SELECTOR, "#content-main > div.app-auth.module > table > tbody > tr.model-group > th > a").click()
        title = login_fixture.find_element(By.CSS_SELECTOR, "#result_list > tbody > tr > th > a").text
        assert title == group_name, f"{title} is not equal."


    def test_user(self, login_fixture):
        username_u = user_name
        password_u = user_password
        login_fixture.find_element(By.CSS_SELECTOR,
        "#content-main > div.app-auth.module > table > tbody > tr.model-user > th > a ").click()

        login_fixture.find_element(By.CSS_SELECTOR,
                    "#content-main > ul > li > a").click()

        login_field = login_fixture.find_element(By.CSS_SELECTOR, "#id_username")
        login_field.send_keys(username_u)
        password_field = login_fixture.find_element(By.ID, "id_password1")
        password_field.send_keys(password_u)
        password_field2 = login_fixture.find_element(By.ID, "id_password2")
        password_field2.send_keys(password_u)
        login_fixture.find_element(By.CSS_SELECTOR,
                                 "#user_form > div > div > input.default").submit()

        login_fixture.find_element(By.CSS_SELECTOR,
                                  "#id_groups_add_all_link").click()
        login_fixture.find_element(By.CSS_SELECTOR,
                                 "#user_form > div > div > input.default").submit()
        with psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='localhost') as connection:
            with connection.cursor() as cur:
                cur.execute(f"""
                    SELECT name FROM auth_group as g
                    LEFT JOIN auth_user_groups ug on g.id = ug.group_id
                    LEFT JOIN auth_user u on ug.user_id = u.id
                    WHERE u.username = '{user_name}'
                """)
                res_group_name = cur.fetchone()[0]
        assert group_name == res_group_name, f"{res_group_name} is not equal."


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


@pytest.mark.usefixtures('db_2')
class Test_group_2:

    @classmethod
    def setup(cls):
        cls.name = "some_very_strange_name"
        cls.changed_name = "another_very_strange_name"

    def test_user_2(self, login_fixture):
        username_u = user_name
        password_u = user_password
        login_fixture.find_element(By.CSS_SELECTOR,
                                 "#content-main > div.app-auth.module > table > tbody > tr.model-user > th > a ").click()

        login_fixture.find_element(By.CSS_SELECTOR,
                                 "#content-main > ul > li > a").click()

        login_field = login_fixture.find_element(By.CSS_SELECTOR, "#id_username")
        login_field.send_keys(username_u)
        password_field = login_fixture.find_element(By.ID, "id_password1")
        password_field.send_keys(password_u)
        password_field2 = login_fixture.find_element(By.ID, "id_password2")
        password_field2.send_keys(password_u)
        login_fixture.find_element(By.CSS_SELECTOR,
                                 "#user_form > div > div > input.default").submit()
        login_fixture.find_element(By.CSS_SELECTOR,
                                 "#id_is_staff").click()
        login_fixture.find_element(By.NAME,
                                 "_save").submit()
        with psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='localhost') as connection:
            with connection.cursor() as cur:
                cur.execute(f"""
                     SELECT username FROM auth_user as u
                     WHERE u.username = '{user_name}'
                 """)
                db_username = cur.fetchone()[0]
        assert user_name == db_username, f"{db_username} is not equal."
        login_fixture.find_element(By.CSS_SELECTOR,
                                 "#user-tools > a:nth-child(4)").click()
        login_fixture.find_element(By.CSS_SELECTOR,
                                 "#content > p:nth-child(3) > a").click()
        login_field = login_fixture.find_element(By.ID, "id_username")
        login_field.send_keys(username_u)
        password_field = login_fixture.find_element(By.ID, "id_password")
        password_field.send_keys(password_u)
        login_fixture.find_element(By.CSS_SELECTOR, "#login-form > div.submit-row > input[type=submit]").submit()
        text = login_fixture.find_element(By.ID, "user-tools").text
        assert f'Welcome, {username_u}'.lower() in text.lower()

    def test_post(self, login_fixture):
        login_fixture.find_element(By.CSS_SELECTOR,
                                 "#content-main > div.app-app.module > table > tbody > tr > th > a").click()
        # login_fixture.find_element(By.CSS_SELECTOR,
        #                          '#changelist-form > p > a.showall').click()
        login_fixture.find_elements(By.XPATH, '//*[@id="result_list"]/tbody/tr')[-1].find_element(By.CSS_SELECTOR,
                                                                                                "th > a").click()
        image_uri = login_fixture.find_element(By.CSS_SELECTOR, "#id_photo").text
        login_fixture.find_element(By.CSS_SELECTOR,
                                 "#post_form > div > div > p > a").click()
        login_fixture.find_element(By.CSS_SELECTOR,
                                 '#content > form > div > input[type=submit]:nth-child(2)').submit()
        login_fixture.find_element(By.CSS_SELECTOR,
                                 "#user-tools > a:nth-child(2)").click()
        last_uri = login_fixture.find_elements(By.XPATH, '/html/body/main/div/div/div/div')[-1].find_element(By.CSS_SELECTOR,
                                                                                                "div > img").get_attribute('src')
        assert image_uri not in last_uri

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
        time.sleep(30)
        response = requests.get(api_url + f'/pet/{petId}')
        assert response.status_code == 200
        assert response.json()['name'] == self.changed_name











