from .base_page import BasePage


class ProductPage(BasePage):

    def add_to_cart(self):
        button_cart = self.browser.find_element(*MainPageLocators.CART_BUTTON)
        button_cart.click()

    def checking_the_product_name(self):
        book = self.browser.find_element(*ProductLocators.BOOK_NAME).text
        book_in_message = self.browser.find_element(*ProductLocators.BOOK_NAME_BASKET).text
        assert book == book_in_message, 'The names are different'


    def price_comparison(self):
        price = self.browser.find_element(*ProductLocators.PRICE).text
        price_in_message = self.browser.find_element(*ProductLocators.PRICE_BASKET).text
        assert price == price_in_message, 'The names are different'

    def should_not_be_success_message(self): #упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"


    def success_message_is_disappeared(self): #будет ждать до тех пор, пока элемент не исчезнет
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but is must disappeare "
