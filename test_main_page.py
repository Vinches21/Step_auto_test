import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.base_page import BasePage



# def test_add_to_cart(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open() # открываем страницу
#     page.add_to_cart()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_the_shopping_cart()
    basket_page = BasketPage(browser, link)
    basket_page.should_be_no_products()
    basket_page.should_be_an_empty_basket()













# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open() # открываем страницу
#     page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()

# def test_guest_should_see_login_link(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()

# def test_quest_login(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     time.sleep(5)
#     page.open()
#     page.go_to_login_page()
#     login_page = LoginPage(browser, link)
#     time.sleep(5)
#     login_page.should_be_login_page()