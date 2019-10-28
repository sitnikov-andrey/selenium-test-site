from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import CartPageLocators

class CartPage(BasePage):
    def should_not_be_items_in_the_cart(self):
        # Проверяет, что в корзине нет покупок. 
        assert self.is_not_element_present(*CartPageLocators.ITEMS_NOT_PRESENT), "Cart not empty"
    
    def should_be_message_about_items_is_absent(self):
        # Проверяет, что сообщение об отсутствии покупок корректно и соответствует требованиям 
        URL = self.browser.current_url
        if 'en-gb' in URL:
            assert self.browser.find_element(*CartPageLocators.MESSAGE_ABOUT_ITEMS_IS_ABSENT).text == "Your basket is empty. Continue shopping", "Message 'Your basket is empty' is absent"