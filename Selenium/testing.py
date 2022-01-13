import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test:
    url = "https://wicenter-test.ddns.net/app/#/login"
    login = "sveta"
    password = "Bler4321!"

    def test_new(self):
        self.driver = webdriver.Chrome("/home/hadus/QA-courses/Selenium/tools/chromedriver")
        self.driver.get(self.url)
        self.driver.maximize_window()

        login_field = self.driver.find_element(By.ID, "username")
        login_field.send_keys(self.login)
        time.sleep(1)
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(self.password)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#login-form > div > div > form > div.signin-footer."
                                                  "modal-audit__footer > button").submit()
        time.sleep(5)

        title = self.driver.find_element(By.CSS_SELECTOR, "#topnav > div.header__menu.header__menu_false "
                                                          "> div:nth-child(6) > div > div > a").text
        assert title == self.login, f"{title} is not equal {self.login}."
        self.driver.quit()
