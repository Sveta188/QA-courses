import pytest
import psycopg2

from selenium.webdriver.common.by import By
from Selenium.sources.variables import *
from Selenium.sources.locators import TestCase1Locators


@pytest.mark.usefixtures('db_1')
class Test_group_1:

    @classmethod
    def setup(cls):
        cls.username = "some_very_strange_username"

    def test_group(self, login_fixture):
        login_fixture.find_element(*TestCase1Locators.EXPECTED_TEST_GROUP).click()
        title = login_fixture.find_element(*TestCase1Locators.TEST_GROUP_IN_SELECT_GROUP).text
        assert title == group_name, f"{title} is not equal."

    def test_user(self, login_fixture):
        username_u = user_name
        password_u = user_password
        login_fixture.find_element(*TestCase1Locators.ADD_USER_BUTTON).click()

        login_fixture.find_element(*TestCase1Locators.PRESS_USER_BUTTON).click()

        login_field = login_fixture.find_element(*TestCase1Locators.ADD_USER_NAME_FIELD)
        login_field.send_keys(username_u)
        password_field = login_fixture.find_element(*TestCase1Locators.ADD_USER_PASSWORD_FIELD)
        password_field.send_keys(password_u)
        password_field2 = login_fixture.find_element(*TestCase1Locators.ADD_USER_PASSWORD_CONFIRMATION_FIELD)
        password_field2.send_keys(password_u)
        login_fixture.find_element(*TestCase1Locators.SAVE_NEW_USER_BUTTON).submit()

        login_fixture.find_element(*TestCase1Locators.FORWARD_ARROW).click()
        login_fixture.find_element(*TestCase1Locators.SUBMIT_BUTTON).submit()
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