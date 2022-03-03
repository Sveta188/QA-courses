import pytest
import psycopg2

from selenium.webdriver.common.by import By
from Selenium.sources.variables import *
from Selenium.sources.locators import TestCase2Locators, TestCase1Locators


@pytest.mark.usefixtures('db_2')
class Test_group_2:

    @classmethod
    def setup(cls):
        cls.name = "some_very_strange_name"
        cls.changed_name = "another_very_strange_name"

    def test_user_2(self, login_fixture):
        username_u = user_name
        password_u = user_password
        login_fixture.find_element(*TestCase2Locators.EXPECTED_TEST_GROUP).click()
        login_fixture.find_element(*TestCase1Locators.PRESS_USER_BUTTON).click()
        login_field = login_fixture.find_element(*TestCase2Locators.ADD_USER_NAME_FIELD)
        login_field.send_keys(username_u)
        password_field = login_fixture.find_element(*TestCase2Locators.ADD_USER_PASSWORD_FIELD)
        password_field.send_keys(password_u)
        password_field2 = login_fixture.find_element(*TestCase2Locators.ADD_USER_PASSWORD_CONFIRMATION_FIELD)
        password_field2.send_keys(password_u)
        login_fixture.find_element(*TestCase1Locators.SAVE_NEW_USER_BUTTON).submit()
        login_fixture.find_element(*TestCase2Locators.ADD_STAFF_STATUS_BTN).click()
        login_fixture.find_element(*TestCase2Locators.SAVE_BUTTON).submit()
        with psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='localhost') as connection:
            with connection.cursor() as cur:
                cur.execute(f"""
                     SELECT username FROM auth_user as u
                     WHERE u.username = '{user_name}'
                 """)
                db_username = cur.fetchone()[0]
        assert user_name == db_username, f"{db_username} is not equal."
        login_fixture.find_element(*TestCase2Locators.LOG_OUT_BTN).click()
        login_fixture.find_element(*TestCase2Locators.LOG_IN).click()
        login_field = login_fixture.find_element(*TestCase2Locators.ADD_USER_NAME_FIELD)
        login_field.send_keys(username_u)
        password_field = login_fixture.find_element(*TestCase2Locators.ADD_USER_PASSWORD_FIELD1)
        password_field.send_keys(password_u)
        login_fixture.find_element(*TestCase2Locators.LOGIN_FORM).submit()
        text = login_fixture.find_element(*TestCase2Locators.TOOLS).text
        assert f'Welcome, {username_u}'.lower() in text.lower()

    def test_post(self, login_fixture):
        login_fixture.find_element(*TestCase2Locators.EXPECTED_TEST_GROUP1).click()
        # login_fixture.find_element(By.CSS_SELECTOR,
        #                          '#changelist-form > p > a.showall').click()
        login_fixture.find_elements(*TestCase2Locators.THE_VERY_LAST_IMAGE)[-1].find_element(By.CSS_SELECTOR,
                                                                                                "th > a").click()
        image_uri = login_fixture.find_element(*TestCase2Locators.IMAGE_URI).text
        login_fixture.find_element(*TestCase2Locators.POSTS_BUTTON).click()
        login_fixture.find_element(*TestCase2Locators.GO_BUTTON).submit()
        login_fixture.find_element(*TestCase2Locators.POST_CLICK).click()
        last_uri = login_fixture.find_elements(*TestCase2Locators.LAST_URI)[-1].find_element(By.CSS_SELECTOR,
                                                                                                "div > img").get_attribute('src')
        assert image_uri not in last_uri
