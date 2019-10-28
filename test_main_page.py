from selenium import webdriver
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
 
def test_guest_can_go_to_login_page(browser):
    # Гость переходит на страницу логина
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()    
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    # Гость переходит в корзину с главной страницы. В ней нет товаров.
    link = "http://selenium1py.pythonanywhere.com"
    page = CartPage(browser, link)
    page.open() 
    page.view_basket_button_click()
    page.should_not_be_items_in_the_cart()
    page.should_be_message_about_items_is_absent()