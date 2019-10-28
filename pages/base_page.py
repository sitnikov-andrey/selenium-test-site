from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators
import math


class BasePage(object):
    def __init__(self, browser, url,  timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        # Нажимает кнопку логина 
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def open(self):
        # Открывает страницу
        self.browser.get(self.url)

    def is_disappeared(self, how, what, timeout=4):
        # Проверяет, что какой-то элемент исчезает
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what):
        # Проверяет существует-ли какой-либо элемент
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        # Проверяет, что элемент не появляется на странице в течение заданного времени
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    
    def should_be_authorized_user(self):
        # Проверяет авторизован-ли пользователь
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"

    def should_be_login_link(self):
        # Проверяет, существует-ли кнопка логина
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def solve_quiz_and_get_code(self):
        # Работает с модальными окнами
        WebDriverWait(self.browser, 3).until(EC.alert_is_present())   
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            # Проверяет существование второго модального окна
            WebDriverWait(self.browser, 4).until(EC.alert_is_present())      
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except (NoAlertPresentException, TimeoutException):
            print("No second alert presented")

    def view_basket_button_click(self):
        # Нажимает кнопку 'добавить в корзину'
        view_basket = self.browser.find_element(*BasePageLocators.VIEW_BASKET_BUTTON)
        view_basket.click()