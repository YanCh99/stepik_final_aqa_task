import pytest                                 # Импортируем фреймворк Pytest для работы с фикстурами и маркерами
import time                                   # Импортируем встроенный модуль time для работы со временем (нужен для генерации email)
from .pages.product_page import ProductPage   # Импортируем класс страницы товара для взаимодействия с ней
from .pages.basket_page import BasketPage     # Импортируем класс страницы корзины для проверок пустоты
from .pages.login_page import LoginPage       # Импортируем класс страницы логина для регистрации пользователя

class TestUserAddToBasketFromProductPage():   # Создаем класс для группировки тестов от лица авторизованного пользователя
    
    @pytest.fixture(scope="function", autouse=True) # Объявляем фикстуру, которая автоматически (autouse=True) запустится перед каждым тестом (scope="function") внутри этого класса
    def setup(self, browser):                 # Метод подготовки данных перед тестом (принимает фикстуру драйвера browser)
        link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/" # Задаем ссылку на страницу регистрации/авторизации
        page = LoginPage(browser, link)       # Создаем объект (Page Object) страницы логина
        page.open()                           # Открываем страницу регистрации в браузере
        
        email = str(time.time()) + "@faker.org" # Генерируем уникальный email, превращая текущее время (в секундах) в строку
        password = "TestPassword7!4739!"      # Задаем надежный пароль (подходящий под требования безопасности сайта)
        page.register_new_user(email, password) # Вызываем метод регистрации, передавая сгенерированные почту и пароль
        page.should_be_authorized_user()      # Проверяем, что после регистрации появилась иконка пользователя (мы успешно залогинены)
            
    def test_user_cant_see_success_message(self, browser): # Тест 1: Юзер не должен видеть сообщение об успехе при открытии товара
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0" # Ссылка на конкретную книгу
        page = ProductPage(browser, link)     # Инициализируем страницу товара
        page.open()                           # Открываем страницу товара
        page.should_not_be_success_message()  # Убеждаемся, что зеленого алерта об успехе нет на экране 
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser): # Тест 2: Юзер может добавить товар в корзину
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0" # Ссылка на ту же книгу
        page = ProductPage(browser, link)     # Инициализируем страницу товара
        page.open()                           # Открываем страницу товара
        page.add_product_to_cart()            # Нажимаем кнопку "Добавить в корзину"
        page.solve_quiz_and_get_code()        # Проходим капчу (алерт с математической задачкой из-за параметра ?promo)
        page.should_be_correct_product_name_in_cart() # Проверяем, что название добавленной книги в алерте совпадает с названием на странице
        page.should_be_cart_price_equals_product_price() # Проверяем, что цена корзины равна цене добавленного товара

# Параметризуем тест для неавторизованного гостя: Pytest запустит тест ниже 10 раз, по очереди подставляя каждую ссылку в переменную link
@pytest.mark.parametrize("link", [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0", # Проверка с параметром offer0
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1", # Проверка с параметром offer1
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2", # Проверка с параметром offer2
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3", # Проверка с параметром offer3
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4", # Проверка с параметром offer4
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5", # Проверка с параметром offer5
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6", # Проверка с параметром offer6
    # Точечно помечаем ссылку offer7 как "ожидаемо падающую" (xfail), так как там баг. Тест упадет, но отчет не покраснеет.
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail(reason="Баг на стороне разработки, номер фикса 112233")),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8", # Проверка с параметром offer8
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"  # Проверка с параметром offer9
])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link): # Функция теста принимает фикстуру browser и переменную link из параметризации
    page = ProductPage(browser, link)         # Инициализируем страницу товара с переданной ссылкой
    page.open()                               # Открываем страницу
    page.add_product_to_cart()                # Нажимаем добавить в корзину
    page.solve_quiz_and_get_code()            # Решаем капчу
    page.should_be_correct_product_name_in_cart() # Проверяем корректность названия товара
    page.should_be_cart_price_equals_product_price() # Проверяем корректность стоимости


def test_guest_cant_see_success_message(browser): # Тест: Гость не видит сообщение об успехе без добавления товара (негативная проверка)
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" # Ссылка без промо-акций
    page = ProductPage(browser, link)         # Инициализируем страницу товара
    page.open()                               # Открываем страницу
    page.should_not_be_success_message()      # Ждем положенное время и убеждаемся, что алерта нет


def test_guest_should_see_login_link_on_product_page(browser): # Тест: Гость видит ссылку на логин на странице товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/" # Ссылка на другую книгу
    page = ProductPage(browser, link)         # Инициализируем страницу товара
    page.open()                               # Открываем страницу
    page.should_be_login_link()               # Проверяем наличие элемента со ссылкой "Войти или зарегистрироваться"


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser): # Тест: Гость может перейти на страницу логина со страницы товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/" # Ссылка на книгу
    page = ProductPage(browser, link)         # Инициализируем страницу товара
    page.open()                               # Открываем страницу
    page.go_to_login_page()                   # Кликаем по ссылке перехода на страницу авторизации


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser): # Тест: Переход с товара в корзину показывает, что она пуста
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/" # Ссылка на книгу
    page = ProductPage(browser, link)         # Инициализируем страницу товара
    page.open()                               # Открываем страницу
    page.go_to_basket_page()                  # Кликаем по кнопке перехода в корзину в шапке сайта
    basket_page = BasketPage(browser, browser.current_url) # Инициализируем страницу корзины, забирая текущий URL из браузера
    basket_page.should_not_be_items_in_basket() # Проверяем, что блока с товарами в DOM-дереве нет (негативная проверка)
    basket_page.should_be_empty_basket_text()   # Проверяем, что отображается текст "Ваша корзина пуста" (позитивная проверка)