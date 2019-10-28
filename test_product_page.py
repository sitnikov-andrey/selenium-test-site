from selenium import webdriver
from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
import time
import pytest

class TestUserAddToCartFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Регистрирует пользователя и переходит на страницу товара
        self.link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        self.page = ProductPage(browser, self.link)
        self.page.open()
        self.page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = 'passwordpassword'
        self.register = LoginPage(browser, self.link)
        self.register.register_new_user(email, password)
        self.register.should_be_authorized_user()
        self.page.open()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        # Пользователь добавляет продукт в корзину
        page = self.page
        page.click_to_button()
        page.solve_quiz_and_get_code()
        page.result_check()
    
    def test_user_cant_see_success_message(self, browser):
        # Пользователь не видит сообщение об успешной покупке не совершая покупку
        check = ProductPage(browser, self.link)
        check.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
    # Гость может добавить продукт в корзину
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()    
    page.click_to_button()
    page.solve_quiz_and_get_code()
    page.result_check()

@pytest.mark.need_review   
def test_guest_can_go_to_login_page_from_product_page(browser):
    # Гость может перейти логин из продуктовой корзины
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    # Гость переходит в корзину со страницы товара. В ней нет товаров.
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = CartPage(browser, link)
    page.open() 
    page.view_basket_button_click()
    page.should_not_be_items_in_the_cart()
    page.should_be_message_about_items_is_absent()
  
def test_guest_cant_see_success_message(browser): 
    # Гость не видит сообщение об успешной покупке не совершая покупку
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    check = ProductPage(browser, link)
    check.should_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    # Гость должен видеть кнопку логина
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

'''
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    # Гость не видит сообщение об успешной покупке совершая покупку. Этот тест падает
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()    
    page.click_to_button()
    page.solve_quiz_and_get_code()
    check = ProductPage(browser, link)
    check.should_not_be_success_message()

def test_message_dissapeared_after_adding_product_to_cart(browser):
    # Ждет, что сообщение об успешной покупке исчезнет. Этот тест падает. 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.click_to_button()
    page.solve_quiz_and_get_code()
    check = ProductPage(browser, link)
    check.waiting_for_element_to_disappear()
'''