import psycopg2
import pytest
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

url = os.getenv("API_URL")
login = os.getenv("API_LOGIN")
aoi_password = os.getenv("API_PASSWORD")
api_url = os.getenv('REMOTE_API_URL')

dbname=os.getenv('DB_NAME')
user=os.getenv('DB_USER')
password=os.getenv('DB_PASSWORD')
host=os.getenv('DB_HOST')

group_name = os.getenv('GROUP_NAME')
user_name = os.getenv('USER_NAME')



@pytest.fixture(scope='class')
def db_1():
    with psycopg2.connect(dbname=dbname, user=user, password=password, host=host) as connection:
        with connection.cursor() as cur:
            cur.execute(f"""INSERT INTO auth_group (name) values ('{group_name}') returning id""")
            id = cur.fetchone()[0]
            connection.commit()
            yield
            cur.execute(f"""DELETE FROM auth_user WHERE username = '{user_name}'""")
            cur.execute(f"""DELETE FROM auth_user_groups WHERE group_id = {id}""")
            cur.execute(f"""DELETE FROM auth_group WHERE name = '{group_name}'""")
            connection.commit()


@pytest.fixture(scope='class')
def db_2():
    with psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='localhost') as connection:
        with connection.cursor() as cur:
            yield
            cur.execute(f"""DELETE FROM auth_user WHERE username = '{user_name}'""")
            connection.commit()

@pytest.fixture
def login_fixture():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-extensions')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(2)
    driver.get(url)
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, "body > main > section > div > p:nth-child(3) > a").click()

    login_field = driver.find_element(By.ID, "id_username")
    login_field.send_keys(login)
    password_field = driver.find_element(By.ID, "id_password")
    password_field.send_keys(aoi_password)
    driver.find_element(By.CSS_SELECTOR, "#login-form > div.submit-row > input[type=submit]").submit()
    yield driver
    driver.quit()
