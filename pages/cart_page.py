from .base_page import BasePage
from .locators import CartPageLocators

class CartPage(BasePage):
    def cart_should_be_empty(self):
        self.empty_cart_message()
        self.item_not_added_to_cart()
        
    def empty_cart_message(self):
        assert self.browser.find_element(*CartPageLocators.BASKET_MESSAGE), "Сообщения о пустой корзине нет"
    
    def item_not_added_to_cart(self):
        assert self.is_not_element_present(*CartPageLocators.BASKET_TITLE), "Есть товар добавленный в корзину, его не должно быть"
        
