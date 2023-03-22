from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(browser):
        link = "http://selenium1py.pythonanywhere.com/"
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = MainPage(browser, link)
        page.open()                      # открываем страницу
        # выполняем метод страницы — переходим на страницу логина
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)#опеределяем, что мы на нужной странице
        login_page.should_be_login_page()# проверяем наличие форм
        
    def test_guest_should_see_login_link(browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
        
    def test_guest_cant_see_product_in_basket_opened_from_main_page (browser):
        link = "http://selenium1py.pythonanywhere.com/"
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket_page()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.cart_should_be_empty()
# когда мы пишем метод, то определяем, с какими данными он работает. Например,
# def метод(а, с):
#         делаем что-нибудь с переменными а и с
# При этом вызвать такой метод мы можем примерно так:
# переменная = метод(б, е)
# То есть название не передаётся жестко. Перед методом open() есть конструктор, который принимает ссылку и передаёт как url.
# Наверное, это путает, но тут важно понимать, что и как передаётся.
