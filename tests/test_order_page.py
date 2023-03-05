import allure

from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка заказа по верхней кнопке с открытием новой страницы по логотипу Яндекса')
    def test_order_from_top_button(self, driver):
        page = OrderPage(driver)
        page.go_to_site()
        page.click_order_top_button()

        page.set_name("Иван")
        page.set_surname("Иванович")
        page.set_address("Москва")
        page.set_metro("1")
        page.set_phone("89991111111")
        page.click_next_button()

        page.set_date("05.05.2023")
        page.set_period("1")
        page.set_black_color()
        page.click_order_button()
        page.click_yes_button()

        page.check_success_order()
        page.click_show_order_button()

        page.click_ya_logo()
        assert len(driver.window_handles) == 2

        driver.quit()

    @allure.title('Проверка заказа по нижней кнопке с открытием страницы по логотипу Самоката')
    def test_order_from_bottom_button(self, driver):
        page = OrderPage(driver)
        page.go_to_site()
        page.click_order_bottom_button()

        page.set_name("Петр")
        page.set_surname("Петров")
        page.set_address("Питер")
        page.set_metro("2")
        page.set_phone("89991111112")
        page.click_next_button()

        page.set_date("05.06.2023")
        page.set_period("2")
        page.set_grey_color()
        page.click_order_button()
        page.click_yes_button()

        page.check_success_order()
        page.click_show_order_button()

        page.click_samokat_logo()
        page.check_samokat_main_page()

        driver.quit()
