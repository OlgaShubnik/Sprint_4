from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys


class OrderPage:
    order_top_button = [By.XPATH, "//div[@class='Header_Nav__AGCXC']//button[text()='Заказать']"]
    order_bottom_button = [By.XPATH, "/html/body/div/div/div/div[4]/div[2]/div[5]/button"]
    name_input = [By.XPATH, "//input[@placeholder='* Имя']"]
    surname_input = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    address_input = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    metro_input = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    phone_input = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    next_button = [By.XPATH, "//button[text()='Далее']"]
    date_input = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    period_input = [By.XPATH, "//div[@class='Dropdown-control']"]
    black_color = [By.ID, "black"]
    grey_color = [By.ID, "grey"]
    order_button = [By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/button[2]"]
    yes_button = [By.XPATH, "//button[text()='Да']"]
    cookie_button = [By.XPATH, "//button[text()='да все привыкли']"]
    success_order_label = [By.XPATH, "/html/body/div/div/div[2]/div[5]/div[contains(text(), 'Заказ оформлен')]"]
    show_order_button = [By.XPATH, "/html/body/div/div/div[2]/div[5]/div[2]/button"]
    samokat_logo = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]
    ya_logo = [By.CLASS_NAME, "Header_LogoYandex__3TSOI"]

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://qa-scooter.praktikum-services.ru/'

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def get_cookie_button(self):
        try:
            return self.driver.find_element(*self.cookie_button)
        except NoSuchElementException:
            return None

    def click_cookie_button(self):
        button = self.get_cookie_button()
        if button is not None:
            button.click()

    def scroll_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*locator))

    def click_order_top_button(self):
        self.click_cookie_button()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.order_top_button))
        self.driver.find_element(*self.order_top_button).click()

    def click_order_bottom_button(self):
        self.click_cookie_button()
        self.scroll_element(self.order_bottom_button)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.order_bottom_button))
        self.driver.find_element(*self.order_bottom_button).click()

    def set_field(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def set_name(self, name):
        self.set_field(self.name_input, name)

    def set_surname(self, surname):
        self.set_field(self.surname_input, surname)

    def set_address(self, address):
        self.set_field(self.address_input, address)

    def set_metro(self, metro):
        self.driver.find_element(*self.metro_input).click()
        self.driver.find_element(By.XPATH, "//ul[@class='select-search__options']/li[" + metro + "]").click()

    def set_phone(self, phone):
        self.set_field(self.phone_input, phone)

    def click_next_button(self):
        self.click_cookie_button()
        self.scroll_element(self.next_button)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.next_button))
        self.driver.find_element(*self.next_button).click()

    def set_date(self, date):
        self.set_field(self.date_input, date)
        self.driver.find_element(*self.date_input).send_keys(Keys.ENTER)

    def set_period(self, period):
        self.driver.find_element(*self.period_input).click()
        self.driver.find_element(By.XPATH, "//div[@class='Dropdown-menu']/div[" + period + "]").click()

    def set_black_color(self):
        self.driver.find_element(*self.black_color).click()

    def set_grey_color(self):
        self.driver.find_element(*self.grey_color).click()

    def click_order_button(self):
        self.click_cookie_button()
        self.driver.find_element(*self.order_button).click()

    def click_yes_button(self):
        self.scroll_element(self.yes_button)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.yes_button))
        self.driver.find_element(*self.yes_button).click()

    def check_success_order(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.success_order_label))

    def click_show_order_button(self):
        self.driver.find_element(*self.show_order_button).click()

    def click_samokat_logo(self):
        self.driver.find_element(*self.samokat_logo).click()

    def check_samokat_main_page(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_contains(self.base_url))

    def click_ya_logo(self):
        self.driver.find_element(*self.ya_logo).click()

    def check_ya_new_window_page(self):
        assert len(self.driver.window_handles) >= 2
        WebDriverWait(self.driver, 5).until(expected_conditions.url_contains("yredirect"))
