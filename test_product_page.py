import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

class TestUserAddToBasketFromProductPage():
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        
        email = str(time.time()) + "@faker.org"
        password = "TestPassword7!4739!"
        page.register_new_user(email, password)
        page.should_be_authorized_user()
            
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()    
    
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_cart()
        page.solve_quiz_and_get_code()
        page.should_be_correct_product_name_in_cart()
        page.should_be_cart_price_equals_product_price()
    




#@pytest.mark.xfail(reason="Баг на стороне разработки, номер фикса 112233")
# @pytest.mark.parametrize("link", [
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#     pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail(reason="Баг на стороне разработки, номер фикса 112233")),
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#     "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
# ])
# def test_guest_can_add_product_to_basket(browser, link):
#      page = ProductPage(browser, link)
#      page.open()
#      page.add_product_to_cart()
#      page.solve_quiz_and_get_code()
#      page.should_be_correct_product_name_in_cart()
#      page.should_be_cart_price_equals_product_price()
# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()
# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page()
# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_basket_page()
    
#     # Инициализируем страницу корзины
#     basket_page = BasketPage(browser, browser.current_url)
#     basket_page.should_not_be_items_in_basket()
#     basket_page.should_be_empty_basket_text() 

# def test_guest_can_add_product_to_basket(browser):
#     link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = ProductPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#     page.open()
#     page.add_product_to_cart()
#     page.solve_quiz_and_get_code()
#     page.should_be_correct_product_name_in_cart()
#     page.should_be_cart_price_equals_product_price()
