from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class FaqPage:
    # локатор первый вопрос
    first_question = [By.XPATH, '//div[@id="accordion__heading-0"]/parent::div']
    first_answer = [By.XPATH, '//div[@id="accordion__panel-0"]//p']
    # локатор воторой вопрос
    second_question = [By.XPATH, '//div[@id="accordion__heading-1"]/parent::div']
    second_answer = [By.XPATH, '//div[@id="accordion__panel-1"]//p']
    # локатор третий вопрос
    third_question = [By.XPATH, '//div[@id="accordion__heading-2"]/parent::div']
    third_answer = [By.XPATH, '//div[@id="accordion__panel-2"]//p']
    # локатор четвертый вопрос
    fourth_question = [By.XPATH, '//div[@id="accordion__heading-3"]/parent::div']
    fourth_answer = [By.XPATH, '//div[@id="accordion__panel-3"]//p']
    # локатор пятый вопрос
    fifth_question = [By.XPATH, '//div[@id="accordion__heading-4"]/parent::div']
    fifth_answer = [By.XPATH, '//div[@id="accordion__panel-4"]//p']
    # локатор шестой вопрос
    sixth_question = [By.XPATH, '//div[@id="accordion__heading-5"]/parent::div']
    sixth_answer = [By.XPATH, '//div[@id="accordion__panel-5"]//p']
    # локатор седьмой вопрос
    seventh_question = [By.XPATH, '//div[@id="accordion__heading-6"]/parent::div']
    seventh_answer = [By.XPATH, '//div[@id="accordion__panel-6"]//p']
    # локатор восьмой вопрос
    eighth_question = [By.XPATH, '//div[@id="accordion__heading-7"]/parent::div']
    eighth_answer = [By.XPATH, '//div[@id="accordion__panel-7"]//p']

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://qa-scooter.praktikum-services.ru/'

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def wait_element(self, locator, time=10):
        WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator))

    def scroll_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*locator))

    def navigate_to_element(self, locator):
        self.scroll_element(locator)
        self.wait_element(locator)

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def check_text(self, locator, expected):
        assert self.driver.find_element(*locator).text == expected

    def navigate_to_first_faq(self):
        self.navigate_to_element(self.first_question)

    def click_first_faq(self):
        self.click_element(self.first_question)

    def check_first_question_text(self):
        self.check_text(self.first_question, 'Сколько это стоит? И как оплатить?')

    def check_first_answer_text(self):
        self.check_text(self.first_answer, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.')

    def navigate_to_second_faq(self):
        self.navigate_to_element(self.second_question)

    def click_second_faq(self):
        self.click_element(self.second_question)

    def check_second_question_text(self):
        self.check_text(self.second_question, 'Хочу сразу несколько самокатов! Так можно?')

    def check_second_answer_text(self):
        self.check_text(self.second_answer, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.')

    def navigate_to_third_faq(self):
        self.navigate_to_element(self.third_question)

    def click_third_faq(self):
        self.click_element(self.third_question)

    def check_third_question_text(self):
        self.check_text(self.third_question, 'Как рассчитывается время аренды?')

    def check_third_answer_text(self):
        self.check_text(self.third_answer, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')

    def navigate_to_fourth_faq(self):
        self.navigate_to_element(self.fourth_question)

    def click_fourth_faq(self):
        self.click_element(self.fourth_question)

    def check_fourth_question_text(self):
        self.check_text(self.fourth_question, 'Можно ли заказать самокат прямо на сегодня?')

    def check_fourth_answer_text(self):
        self.check_text(self.fourth_answer, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.')

    def navigate_to_fifth_faq(self):
        self.navigate_to_element(self.fifth_question)

    def click_fifth_faq(self):
        self.click_element(self.fifth_question)

    def check_fifth_question_text(self):
        self.check_text(self.fifth_question, 'Можно ли продлить заказ или вернуть самокат раньше?')

    def check_fifth_answer_text(self):
        self.check_text(self.fifth_answer, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.')

    def navigate_to_sixth_faq(self):
        self.navigate_to_element(self.sixth_question)

    def click_sixth_faq(self):
        self.click_element(self.sixth_question)

    def check_sixth_question_text(self):
        self.check_text(self.sixth_question, 'Вы привозите зарядку вместе с самокатом?')

    def check_sixth_answer_text(self):
        self.check_text(self.sixth_answer, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.')

    def navigate_to_seventh_faq(self):
        self.navigate_to_element(self.seventh_question)

    def click_seventh_faq(self):
        self.click_element(self.seventh_question)

    def check_seventh_question_text(self):
        self.check_text(self.seventh_question, 'Можно ли отменить заказ?')

    def check_seventh_answer_text(self):
        self.check_text(self.seventh_answer, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.')

    def navigate_to_eighth_faq(self):
        self.navigate_to_element(self.eighth_question)

    def click_eighth_faq(self):
        self.click_element(self.eighth_question)

    def check_eighth_question_text(self):
        self.check_text(self.eighth_question, 'Я жизу за МКАДом, привезёте?')

    def check_eighth_answer_text(self):
        self.check_text(self.eighth_answer, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
