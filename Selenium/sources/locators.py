
from selenium.webdriver.common.by import By


class WebAppLocators:

    GO_TO_ADMIN_BTN = (By.LINK_TEXT, 'Go to Admin')

    USERNAME_FIELD = (By.CSS_SELECTOR, "input[type='text']")

    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[type="password"]')

    LOGIN_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"]')

    LIST_OF_GROUPS = (By.LINK_TEXT, 'Groups')


class TestCase1Locators:

    EXPECTED_TEST_GROUP = (By.CSS_SELECTOR, "#content-main > div.app-auth.module > table > tbody > tr.model-group > th > a")

    TEST_GROUP_IN_SELECT_GROUP = (By.CSS_SELECTOR, "#result_list > tbody > tr > th > a")

    ADD_USER_BUTTON = (By.CSS_SELECTOR, "#content-main > div.app-auth.module > table > tbody > tr.model-user > th > a")

    PRESS_USER_BUTTON = (By.CSS_SELECTOR,  "#content-main > ul > li > a")

    ADD_USER_NAME_FIELD = (By.CSS_SELECTOR, "#id_username")

    ADD_USER_PASSWORD_FIELD = (By.ID, "id_password1")

    ADD_USER_PASSWORD_CONFIRMATION_FIELD = (By.ID, "id_password2")

    SAVE_NEW_USER_BUTTON = (By.CSS_SELECTOR, "#user_form > div > div > input.default")

    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#user_form > div > div > input.default")

    FORWARD_ARROW = (By.CSS_SELECTOR, "#id_groups_add_all_link")


class TestCase2Locators:
    EXPECTED_TEST_GROUP = (By.CSS_SELECTOR,
                           "#content-main > div.app-auth.module > table > tbody > tr.model-user > th > a ")

    ADD_STAFF_STATUS_BTN = (By.CSS_SELECTOR, "#id_is_staff")

    ADD_USER_PASSWORD_CONFIRMATION_FIELD = (By.ID, "id_password2")

    EXPECTED_TEST_GROUP1 = (By.CSS_SELECTOR,
                                 "#content-main > div.app-app.module > table > tbody > tr > th > a")

    ADD_USER_PASSWORD_FIELD = (By.ID, "id_password1")

    ADD_USER_PASSWORD_FIELD1 = (By.ID, "id_password")

    SAVE_BUTTON = (By.NAME, "_save")

    LOG_OUT_BTN = (By.CSS_SELECTOR, "#user-tools>a:nth-child(4)")

    LOG_IN = (By.CSS_SELECTOR, "#content > p:nth-child(3) > a")

    ADD_USER_NAME_FIELD = (By.CSS_SELECTOR, "#id_username")

    LOGIN_FORM = (By.CSS_SELECTOR, "#login-form > div.submit-row > input[type=submit]")

    TOOLS = (By.ID, "user-tools")

    THE_VERY_LAST_IMAGE = (By.XPATH, '//*[@id="result_list"]/tbody/tr')

    IMAGE_URI = (By.CSS_SELECTOR, "#id_photo")

    POSTS_BUTTON = (By.CSS_SELECTOR, "#post_form > div > div > p > a")

    GO_BUTTON = (By.CSS_SELECTOR,'#content > form > div > input[type=submit]:nth-child(2)')

    YES_IM_SURE_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"]')

    ADD_USER_BUTTON = (By.CSS_SELECTOR, ".model-user>td>.addlink")

    POST_CLICK = (By.CSS_SELECTOR, "#user-tools > a:nth-child(2)")

    LAST_URI = (By.XPATH, '/html/body/main/div/div/div/div')