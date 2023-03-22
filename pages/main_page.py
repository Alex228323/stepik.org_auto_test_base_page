# тут мы храним методы по конкретной странице, 
# завернутые в класс этой странице. Класс этот - 
# условный MainPage - наследник класса BasePage, 
# чтобы можно было пользоваться методами, описанными 
# в base_page.py
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage
# класс  MainPage. Его нужно сделать наследником класса BasePage. Класс-предок в Python указывается в скобках


class MainPage(BasePage):
    pass