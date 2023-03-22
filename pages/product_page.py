from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.add_to_basket).click()
    
    def message_about_adding_an_item_to_the_cart(self):
        assert self.is_not_element_present(*ProductPageLocators.message_add_to_basket), "Сообщения о добавлении в корзину есть, а не должно"
        
    def should_disappear(self):
        # проверка, что элемент исчез
        assert self.is_disappeared(*ProductPageLocators.message_add_to_basket), "Сообщение не исчезло, хотя должно"
        
    def book_name_match_from_alert(self):
        book = self.browser.find_element(*ProductPageLocators.book_name)
        book_name_check = self.browser.find_element(*ProductPageLocators.book_name_check)
        assert book.text == book_name_check.text, "Названия книг не совпадают"
    
    def match_the_value_of_the_basket_with_the_price_of_the_product(self):
        product_price = self.browser.find_element(*ProductPageLocators.product_price)
        price_number = self.browser.find_element(*ProductPageLocators.price_number)
        assert product_price.text == price_number.text, "Цена в корзине и цена товара не совпадают"