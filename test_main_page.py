from .pages.main_page import MainPage       # Импортируем класс главной страницы для использования её методов
from .pages.basket_page import BasketPage   # Импортируем класс страницы корзины для проверок внутри корзины
from .pages.login_page import LoginPage     # Импортируем класс страницы логина для работы с формами авторизации
import pytest                               # Импортируем библиотеку pytest для работы с тестами и маркерами

@pytest.mark.login_guest                    # Маркируем класс тестов меткой 'login_guest' для возможности выборочного запуска
class TestLoginForMainPage():               # Создаем класс для группировки тестов логина с главной страницы
    
    def test_guest_can_go_to_login_page(self, browser):           # Тест: гость может перейти на страницу логина (передаем фикстуру browser)
        link = "http://selenium1py.pythonanywhere.com/"           # Сохраняем URL главной страницы в переменную link
        page = MainPage(browser, link)                            # Инициализируем объект главной страницы (Page Object), передаем драйвер и URL
        page.open()                                               # Открываем страницу в браузере с помощью метода базовой страницы
        page.go_to_login_page()                                   # Выполняем клик по ссылке "Войти или зарегистрироваться"
        login_page = LoginPage(browser, browser.current_url)      # Инициализируем страницу логина, получая текущий URL из браузера после клика
        login_page.should_be_login_page()                         # Проверяем корректность страницы логина (URL и наличие обеих форм)

    def test_guest_should_see_login_link(self, browser):          # Тест: гость видит ссылку на логин
        link = "http://selenium1py.pythonanywhere.com/"           # Сохраняем URL главной страницы
        page = MainPage(browser, link)                            # Инициализируем объект главной страницы
        page.open()                                               # Открываем страницу в браузере
        page.should_be_login_link()                               # Проверяем, что элемент ссылки на логин присутствует в DOM-дереве страницы
    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):  # Тест: гость не видит товары в пустой корзине
    link = "https://selenium1py.pythonanywhere.com/"              # Сохраняем URL главной страницы
    page = MainPage(browser, link)                                # Инициализируем объект главной страницы
    page.open()                                                   # Открываем страницу в браузере
    page.go_to_basket_page()                                      # Кликаем по кнопке корзины в шапке сайта для перехода
    basket_page = BasketPage(browser, browser.current_url)        # Инициализируем страницу корзины, передавая новый URL из браузера
    basket_page.should_not_be_items_in_basket()                   # Ожидаем, что блок с товарами отсутствует (негативная проверка)
    basket_page.should_be_empty_basket_text()                     # Ожидаем, что на странице есть текст "Ваша корзина пуста" (позитивная проверка)