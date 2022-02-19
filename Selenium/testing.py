import os
import time

import pytest
import psycopg2

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
        self.driver = webdriver.Chrome(service=Service(self.driver_path), options=chrome_options)
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
                                 "#id_groups_from > option").click()
        self.driver.find_element(By.ID,
                                 "id_groups_add_link").click()
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


