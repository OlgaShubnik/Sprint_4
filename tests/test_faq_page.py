import allure

from selenium import webdriver
from pages.faq_page import FaqPage


class TestFaqPage:
    driver = None
    page = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.page = FaqPage(cls.driver)
        cls.page.go_to_site()

    @allure.title('Проверка 1 вопроса')
    def test_first_faq(self):
        self.page.navigate_to_first_faq()
        self.page.click_first_faq()
        self.page.check_first_question_text()
        self.page.check_first_answer_text()

    @allure.title('Проверка 2 вопроса')
    def test_second_faq(self):
        self.page.navigate_to_second_faq()
        self.page.click_second_faq()
        self.page.check_second_question_text()
        self.page.check_second_answer_text()

    @allure.title('Проверка 3 вопроса')
    def test_third_faq(self):
        self.page.navigate_to_third_faq()
        self.page.click_third_faq()
        self.page.check_third_question_text()
        self.page.check_third_answer_text()

    @allure.title('Проверка 4 вопроса')
    def test_fourth_faq(self):
        self.page.navigate_to_fourth_faq()
        self.page.click_fourth_faq()
        self.page.check_fourth_question_text()
        self.page.check_fourth_answer_text()

    @allure.title('Проверка 5 вопроса')
    def test_fifth_faq(self):
        self.page.navigate_to_fifth_faq()
        self.page.click_fifth_faq()
        self.page.check_fifth_question_text()
        self.page.check_fifth_answer_text()

    @allure.title('Проверка 6 вопроса')
    def test_sixth_faq(self):
        self.page.navigate_to_sixth_faq()
        self.page.click_sixth_faq()
        self.page.check_sixth_question_text()
        self.page.check_sixth_answer_text()

    @allure.title('Проверка 7 вопроса')
    def test_seventh_faq(self):
        self.page.navigate_to_seventh_faq()
        self.page.click_seventh_faq()
        self.page.check_seventh_question_text()
        self.page.check_seventh_answer_text()

    @allure.title('Проверка 8 вопроса')
    def test_eighth_faq(self):
        self.page.navigate_to_eighth_faq()
        self.page.click_eighth_faq()
        self.page.check_eighth_question_text()
        self.page.check_eighth_answer_text()

    @classmethod
    def teardown_class(cls):
        # закрой браузер
        cls.driver.quit()
