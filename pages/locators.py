from selenium.webdriver.common.by import By

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "a[class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class CartPageLocators(object):
    ITEMS_NOT_PRESENT = (By.CSS_SELECTOR, "h2[class='col-sm-6 h3']")
    MESSAGE_ABOUT_ITEMS_IS_ABSENT = (By.CSS_SELECTOR, "div[id='content_inner'] > p")

class LoginPageLocators(object):
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='registration-email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='registration-password1']")
    PASSWODR_CONFIRM_INPUT = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")

class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")

class ProductPageLocators(object):
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    NAME_IN_MESSAGE = (By.CSS_SELECTOR, "div[class='alertinner '] > strong")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "div[class='alertinner '] > p > strong")
    PRICE = (By.CSS_SELECTOR, "p[class='price_color']")
    BOOK_NAME = (By.CSS_SELECTOR, "div[class='col-sm-6 product_main'] > h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div[class='alertinner ']")
