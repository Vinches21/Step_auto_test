import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.mark.skip
@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                    pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    browser.implicitly_wait(10)
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = MainPage(browser, link)
    page.open()
    prod_page = ProductPage(browser, link)
    prod_page.add_to_cart()
    prod_page.solve_quiz_and_get_code()
    prod_page.checking_the_product_name()
    prod_page.price_comparison()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    prod_page = ProductPage(browser, link)
    prod_page.add_to_cart()
    prod_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    prod_page = ProductPage(browser, link)
    prod_page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    prod_page = ProductPage(browser, link)
    prod_page.add_to_cart()
    prod_page.success_message_is_disappeared()