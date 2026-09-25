from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket items are presented, but shouldn`t be"
        
    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "Empty basket message is not presented"