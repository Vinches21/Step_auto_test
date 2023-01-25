import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage



def test_guest_can_add_product_to_basket(browser):
    browser.implicitly_wait(10)
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу
    prod_page = ProductPage(browser, link)
    prod_page.add_to_cart()
    prod_page.solve_quiz_and_get_code()
    prod_page.checking_the_product_name()
    prod_page.price_comparison()
    # time.sleep(2)