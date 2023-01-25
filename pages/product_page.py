import time

from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import *
from .login_page import  LoginPage


class ProductPage(BasePage):

    def add_to_cart(self):
        button_cart = self.browser.find_element(*MainPageLocators.CART_BUTTON)
        button_cart.click()

    def checking_the_product_name(self):
        book = self.browser.find_element(*ProductLocators.BOOK_NAME).text
        print(book)
        book_in_message = self.browser.find_element(*ProductLocators.BOOK_NAME_BASKET).text
        assert book == book_in_message, 'The names are different'
        print(book_in_message)


    def price_comparison(self):
        price = self.browser.find_element(*ProductLocators.PRICE).text
        print(price)
        price_in_message = self.browser.find_element(*ProductLocators.PRICE_BASKET).text
        assert price == price_in_message, 'The names are different'
        print(price_in_message)