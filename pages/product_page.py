import math
from .base_page import BasePage
#from .locators import 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    
# 1. Метод для ДЕЙСТВИЯ    
    def add_product_to_cart(self):
        assert self.is_element_present(By.CSS_SELECTOR, ".btn-add-to-basket"),"Add to basket button is not presented"
        add_to_cart_button = self.browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        add_to_cart_button.click()
    
# 2. Метод для ПРОВЕРКИ имени книги        
    def should_be_correct_product_name_in_cart(self):
        assert self.is_element_present(By.CSS_SELECTOR, ".alert-success .alertinner strong"), "Success banner is not presented"
        assert self.is_element_present(By.CSS_SELECTOR, "h1"), "Book name is not presented on page"
        
        add_to_cart_banner_with_name = self.browser.find_element(By.CSS_SELECTOR, ".alert-success .alertinner strong")
        book_name = self.browser.find_element(By.CSS_SELECTOR, "h1")
        
        actual_book_name = book_name.text
        assert actual_book_name == add_to_cart_banner_with_name.text , "Book name in cart does not match the actual book name"

# 3. Метод для ПРОВЕРКИ цены
    def should_be_cart_price_equals_product_price(self):
        assert self.is_element_present(By.CSS_SELECTOR, ".alert-info .alertinner strong"), "Cart price alert is not presented"
        assert self.is_element_present(By.CSS_SELECTOR, ".product_main .price_color"), "Product price is not presented"
        
        cart_price = self.browser.find_element(By.CSS_SELECTOR,".alert-info .alertinner strong")
        book_price = self.browser.find_element(By.CSS_SELECTOR,".product_main .price_color")
        
        actual_cart_price = cart_price.text
        actual_book_price = book_price.text
        
        assert actual_cart_price == actual_book_price, "Cart price is not match the book price"
        

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
