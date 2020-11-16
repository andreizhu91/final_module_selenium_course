from .base_page import BasePage
from .product_page import ProductPage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(ProductPage):
    def should_be_basket_empty(self):
        assert self.is_not_element_present \
            (*BasketPageLocators.LIST_PRODUCTS_IN_BASKET), \
                "Fail, basket don't empty"

    def should_be_message_about_basket_empty(self):
        assert "Your basket is empty" in self.browser.find_element \
            (*BasketPageLocators.MESSAGE_ABOUT_BASKET_EMPTY).text, \
                "Fail message about basket empty"
