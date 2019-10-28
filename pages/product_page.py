from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def add_to_basket(self):
        self.click_to_button()

    def click_to_button(self):
        # Поиск кнопки добавления в корзину
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()

    def result_check(self):
        # Проверяет, что сообщения об успешной покупке корректны и соответствуют требованиям  
        URL = self.browser.current_url
        if 'en-gb' in URL:
            time.sleep(2)
            book_name_in_the_message = self.browser.find_element(*ProductPageLocators.NAME_IN_MESSAGE)
            book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
            price_in_the_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE)
            price = self.browser.find_element(*ProductPageLocators.PRICE)
            assert book_name_in_the_message.text == book_name.text, "Book titles do not match"
            assert price_in_the_message.text == price.text, "Prices do not match"

    def should_not_be_success_message(self):
        # Проверяет наличие сообщение об успешной покупке. Его быть не должно.
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
    
    def waiting_for_element_to_disappear(self):
        # Проверяет, что сообщение об успешной покупке исчезло.
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "The element has not disappeared"



            