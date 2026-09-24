from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_correct_product_name_in_cart()
    page.should_be_cart_price_equals_product_price()