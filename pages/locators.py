# тут мы храним локаторы, в виде констант. 
# Локаторы каждой отдельной страницы завёрнуты 
# в класс, чтобы было удобно импортировать
from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class CartPageLocators():
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_TITLE = (By.CSS_SELECTOR, ".basket-title")
    
class LoginPageLocators():
    login_form = (By.CSS_SELECTOR, "#login_form")
    register_form = (By.CSS_SELECTOR, "#register_form")
    login_page_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    email_input = (By.ID, "id_registration-email")
    password1_input = (By.ID, "id_registration-password1")
    password2_input = (By.ID, "id_registration-password2")
    register_button = (By.NAME, "registration_submit")
    
class ProductPageLocators():
    add_to_basket = (By.CLASS_NAME, "btn-add-to-basket")
    book_name_check = (By.CSS_SELECTOR, ".product_main h1")
    book_name = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    price_number = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    product_price = (By.CSS_SELECTOR, ".product_main .price_color")
    message_add_to_basket = (By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")