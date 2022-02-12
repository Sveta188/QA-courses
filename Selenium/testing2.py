import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test:

    def test_registration(self):
        driver = webdriver.Chrome("/home/hadus/QA-courses/Selenium/tools/chromedriver")
        driver.get('http://demo.guru99.com/test/newtours/register.php')

        driver.find_element(By.NAME, 'firstName').send_keys('Iftikhar')
        driver.find_element(By.NAME, 'lastName').send_keys('Ahmad')
        driver.find_element(By.NAME, 'phone').send_keys('+375445678901')
        driver.find_element(By.NAME, 'userName').send_keys('hadus')
        driver.find_element(By.NAME, 'address1').send_keys('Chto-to')
        driver.find_element(By.NAME, 'city').send_keys('Minsk')
        driver.find_element(By.NAME, 'state').send_keys('Minsk region')
        driver.find_element(By.NAME, 'postalCode').send_keys('220014')
        driver.find_element(By.NAME, 'country').send_keys('BELARUS')
        driver.find_element(By.NAME, 'email').send_keys('testgfhej@gmail.com')
        driver.find_element(By.NAME, 'password').send_keys('123123')
        driver.find_element(By.NAME, 'confirmPassword').send_keys('123123')
        driver.find_element(By.NAME, 'submit').submit
        time.sleep(2)
        driver.quit()


    def test_correct_first_last_name(self):
        driver = webdriver.Chrome("/home/hadus/QA-courses/Selenium/tools/chromedriver")
        driver.get('https://demo.guru99.com/test/newtours/register_sucess.php')
        first_last_name = driver.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/p[1]/font/b')
        assert "Iftikhar Ahmad" in first_last_name.text
        time.sleep(2)

    def test_correct_username(self):
        driver = webdriver.Chrome("/home/hadus/QA-courses/Selenium/tools/chromedriver")
        driver.get('https://demo.guru99.com/test/newtours/register_sucess.php')
        user_name = driver.find_element(By.XPATH, '//tr[3]/td/p[3]/font/b')
        assert "Iftikharahmad" in user_name.text
        time.sleep(2)

        driver.close()