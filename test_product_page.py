from .pages.product_page import ProductPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
from .pages.locators import LoginPageLocators
import pytest
# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

# def test_guest_can_add_product_to_basket(browser, link):
#     # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page = ProductPage(browser, link)
#     page.open()  
#     page.message_about_adding_an_item_to_the_cart()
#     page.add_to_cart()  
#     page.solve_quiz_and_get_code()
#     page.book_name_match_from_alert()
#     page.match_the_value_of_the_basket_with_the_price_of_the_product()
class TestUserAddToBasketFromProductPage():   
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, timeout=5):
        link = LoginPageLocators.login_page_link # ссылка на страницу логина\регистрации
        self.browser = browser
        # неявное ожидание
        self.browser.implicitly_wait(timeout)
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес	
        page = LoginPage(browser, link)
	    # открываем нужную страницу
        page.open()
        # генерим тестовую почту, задаем пароль 
        email, password = page.make_email_and_pass()
        # регистрируем нового пользователя
        page.register_new_user(email, password)
        # проверяем, что пользователь авторизован
        page.should_be_authorized_user() # на деле такие проверки лучше не делать (setup не для этого)
        
    
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open() 
        page.message_about_adding_an_item_to_the_cart()
        
    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open() 
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        page.match_the_value_of_the_basket_with_the_price_of_the_product()
        page.book_name_match_from_alert()
        

@pytest.mark.need_review  
def test_guest_can_add_product_to_cart(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open() 
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        page.match_the_value_of_the_basket_with_the_price_of_the_product()
        page.book_name_match_from_alert()   
        
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open() 
    page.add_to_cart()
    page.message_about_adding_an_item_to_the_cart()
  
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open() 
    page.message_about_adding_an_item_to_the_cart()
    
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open() 
    page.add_to_cart()
    page.should_disappear()
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
@pytest.mark.need_review    
def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)#опеределяем, что мы на нужной странице
    login_page.should_be_login_page()# проверяем наличие форм

@pytest.mark.need_review  
def test_guest_cant_see_product_in_basket_opened_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.cart_should_be_empty()
    