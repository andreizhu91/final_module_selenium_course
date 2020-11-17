from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators, BasePageLocators, BasketPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(\
            *ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()
        #self.solve_quiz_and_get_code()

    def go_to_basket_from_product_page(self):
        basket = self.browser.find_element(*BasePageLocators.BASKET)
        basket.click()

    def should_be_message_added_product(self):
        message_product_name = self.browser.find_element(\
            *ProductPageLocators.MESSAGE_PRODUCT_NAME)
        product_name = self.browser.find_element(\
            *ProductPageLocators.PRODUCT_NAME)
        assert product_name.text == message_product_name.text, \
            "Product name in message does not equally product name page"

    def should_be_basket_price_is_equal_to_product_price(self):
        basket_total_is_now = self.browser.find_element(\
            *ProductPageLocators.MESSAGE_BASKET_TOTAL_IS_NOW)
        product_price = self.browser.find_element(\
            *ProductPageLocators.PRODUCT_PRICE)
        assert product_price.text == basket_total_is_now.text, \
            "Basket total does not equally product price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def should_is_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should is disappearede"

    def should_be_see_product_in_basket_opened_from_product_page(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET)
        basket_link.click()
        assert self.is_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "Fail, don't see product in basket"

    def go_to_login_page_from_product_page(self):
        try:
            login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
            login_link.click()
        except NoSuchElementException:
            assert self.browser.current_url == 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/', \
				"Fail, opened not login page"
