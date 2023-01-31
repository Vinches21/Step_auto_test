from pages.base_page import BasePage
from pages.locators import BasketLocators


class BasketPage(BasePage):
    """Проверка что есть текст о том что Корзина пуста"""
    def should_be_an_empty_basket(self):
        assert self.is_element_present(*BasketLocators.MESSAGE_EMPTY), \
            'Нет текста о том что корзина пуста'


    """Проверка что в корзине нет товаров"""
    def should_be_no_products(self):
        assert self.is_not_element_present(*BasketLocators.MESSAGE_PRODUCTS_IN_BASKET), \
        'Товары есть в корзине'

