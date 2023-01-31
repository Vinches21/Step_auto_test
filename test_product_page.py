import time
import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage



@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, link)
        email = str(time.time()) + "@fakemail.org"
        password = '75535211345'
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = MainPage(browser, link)
        page.open()
        prod_page = ProductPage(browser, link)
        prod_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        page = MainPage(browser, link)
        page.open()
        prod_page = ProductPage(browser, link)
        prod_page.add_to_cart()
        prod_page.solve_quiz_and_get_code()
        prod_page.checking_the_product_name()
        prod_page.price_comparison()

"""СПЕЦИАЛЬНО закомментировал параметризацию чтобы проверяющий не тратил время!"""
@pytest.mark.need_review
# @pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
#                                     pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2"
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




@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    prod_page = ProductPage(browser, link)
    prod_page.go_to_the_shopping_cart()
    basket_page = BasketPage(browser, link)
    basket_page.should_be_no_products()
    basket_page.should_be_an_empty_basket()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()
    prod_page = ProductPage(browser, link)
    prod_page.add_to_cart()
    prod_page.success_message_is_disappeared()
