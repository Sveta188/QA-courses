import os
import time
import json
import pytest
import psycopg2
import requests
import uuid

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager




@pytest.mark.usefixtures('db')
class Test:
    url = "http://localhost:8000/"
    login = "admin"
    password = "password"
    driver_path = os.getcwd() + '/tools/chromedriver'
    api_url = "https://petstore.swagger.io/v2"

    @classmethod
    def setup_class(cls):
        cls.group_name = 'test_nam1e'
        cls.user_name = 'test_user'

    @pytest.fixture(scope='class')
    def db(self):
        with psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='localhost') as connection:
            with connection.cursor() as cur:
                cur.execute(f"""INSERT INTO auth_group (name) values ('{self.group_name}') returning id""")
                id = cur.fetchone()[0]
                connection.commit()
                yield
                cur.execute(f"""DELETE FROM auth_user WHERE username = '{self.user_name}'""")
                cur.execute(f"""DELETE FROM auth_user_groups WHERE group_id = {id}""")
                cur.execute(f"""DELETE FROM auth_group WHERE name = '{self.group_name}'""")
                connection.commit()

    @pytest.fixture
    def login_fixture(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-extensions')
        print(self.driver_path)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.implicitly_wait(2)
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.find_element(By.CSS_SELECTOR, "body > main > section > div > p:nth-child(3) > a").click()

        login_field = self.driver.find_element(By.ID, "id_username")
        login_field.send_keys(self.login)
        password_field = self.driver.find_element(By.ID, "id_password")
        password_field.send_keys(self.password)
        self.driver.find_element(By.CSS_SELECTOR, "#login-form > div.submit-row > input[type=submit]").submit()
        yield
        self.driver.quit()

    def test_group(self, login_fixture):
        # db.execute(f"""INSERT INTO auth_group (name) values ('{self.group_name}')""")
        self.driver.find_element(By.CSS_SELECTOR, "#content-main > div.app-auth.module > table > tbody > tr.model-group > th > a").click()
        title = self.driver.find_element(By.CSS_SELECTOR, "#result_list > tbody > tr > th > a").text
        assert title == self.group_name, f"{title} is not equal."


    def test_user(self, login_fixture):
        username_u = self.user_name
        password_u = "YFhjgbgdG3$%^gvf54ef"
        self.driver.find_element(By.CSS_SELECTOR,
        "#content-main > div.app-auth.module > table > tbody > tr.model-user > th > a ").click()

        self.driver.find_element(By.CSS_SELECTOR,
                    "#content-main > ul > li > a").click()

        login_field = self.driver.find_element(By.CSS_SELECTOR, "#id_username")
        login_field.send_keys(username_u)
        password_field = self.driver.find_element(By.ID, "id_password1")
        password_field.send_keys(password_u)
        password_field2 = self.driver.find_element(By.ID, "id_password2")
        password_field2.send_keys(password_u)
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#user_form > div > div > input.default").submit()

        self.driver.find_element(By.CSS_SELECTOR,
                                  "#id_groups_add_all_link").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#user_form > div > div > input.default").submit()
        with psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='localhost') as connection:
            with connection.cursor() as cur:
                cur.execute(f"""
                    SELECT name FROM auth_group as g
                    LEFT JOIN auth_user_groups ug on g.id = ug.group_id
                    LEFT JOIN auth_user u on ug.user_id = u.id
                    WHERE u.username = '{self.user_name}'
                """)
                group_name = cur.fetchone()[0]
        assert self.group_name == group_name, f"{group_name} is not equal."


    def test_api_user(self):
        username = uuid.uuid4().hex
        print(username)
        response = requests.post(self.api_url + "/user", json={
          "id": 0,
          "username": username,
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
        time.sleep(2)
        assert requests.get(self.api_url + "/user/login", params={"username": username, "password": "string"}).status_code == 200
        time.sleep(2)
        assert requests.get(self.api_url + f'/user/{username}').status_code == 200
        time.sleep(2)
        assert requests.get(self.api_url + "/user/logout").status_code == 200
        time.sleep(2)
        assert requests.delete(self.api_url + f'/user/{username}').status_code == 200
        time.sleep(2)


    def test_api_pet(self):
        name = uuid.uuid4().hex
        print(name)
        response = requests.post(self.api_url + "/pet", json={
                "id": 0,
                "category": {
                    "id": 0,
                    "name": "string"
                },
                "name": name,
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
        assert response.status_code == 200
        petId = response.json()['id']
        print(petId)
        assert requests.get(self.api_url + f'/pet/{petId}').status_code == 200
        time.sleep(2)
        assert requests.post(self.api_url + f"/pet/{petId}", data={
                "name": "hgvhjhgfyujbvftyujbfyujftyujbvfgcfyujhfdrftyhvcxdtyuikouytdxcvhjhghiuyfdtyujhfcdft",
                "status": "available"

        },
        headers={
            "accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded"
        }).status_code == 200
        time.sleep(2)
        response = requests.get(self.api_url + f'/pet/{petId}')
        assert response.status_code == 200
        assert response.json()['name'] == "hgvhjhgfyujbvftyujbfyujftyujbvfgcfyujhfdrftyhvcxdtyuikouytdxcvhjhghiuyfdtyujhfcdft"








