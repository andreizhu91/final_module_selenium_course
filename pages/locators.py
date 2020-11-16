from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form>:nth-child(7)")
    
class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    MESSAGE_BASKET_TOTAL_IS_NOW = (By.CSS_SELECTOR, ".alertinner>p>strong")
    MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages>:nth-child(1)>.alertinner>strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, ".btn-group>:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    MESSAGE_ABOUT_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")
    LIST_PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket-title.hidden-xs")
