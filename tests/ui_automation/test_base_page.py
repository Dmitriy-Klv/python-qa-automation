import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

LOGO_LOCATOR = 'img[alt="IT Career Hub"]'
PROGRAMS_TEXT = 'a[href="#submenu:more"] .tn-atom__button-text'
PAYMENT_TEXT = 'a[href="#rec1921734713"] .tn-atom__button-content'
ABOUT_US_TEXT = 'a[href="#submenu:more2"] .tn-atom__button-text'
CONTACTS_TEXT = 'a[href="/ru/contact-us"]'
REVIEWS_TEXT = 'div[data-elem-id="1773659569108000001"] .tn-atom__button-text'
BLOG_TEXT = 'div[data-elem-id="176285426168494440"] .tn-atom__button-text'
LANG_SWITCH_RU = 'a[href="/ru"] .tn-atom__button-text'
LANG_SWITCH_DE = 'div[data-elem-id="1710153064158"]'
CALLBACK_BTN = 'a[href="#popup:form-tr"] .tn-atom__button-text'
CONSULTATION_TEXT = 'div[field="tn_text_175871291756015470"]'


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.get("https://itcareerhub.de/ru")
    driver.implicitly_wait(5)

    yield driver
    driver.quit()


class TestMainPage:

    # Solution option for task 1
    def test_all_elements_are_displayed(self, driver):
        HEADER_ELEMENTS = [
            LOGO_LOCATOR,
            PROGRAMS_TEXT,
            PAYMENT_TEXT,
            ABOUT_US_TEXT,
            REVIEWS_TEXT,
            BLOG_TEXT,
            LANG_SWITCH_RU,
            LANG_SWITCH_DE,
        ]

        for locator in HEADER_ELEMENTS:
            element = driver.find_element(By.CSS_SELECTOR, locator)

            assert element.is_displayed()

    # Solution option for task 2
    def test_programs_text_is_displayed(self, driver):
        logo = driver.find_element(By.CSS_SELECTOR, LOGO_LOCATOR)

        assert logo.is_displayed(), "The Logo is not displayed on the page"


    def test_programs_is_displayed(self, driver):
        programs = driver.find_element(By.CSS_SELECTOR, PROGRAMS_TEXT)

        assert programs.is_displayed(), "The Programs is not displayed on the page"


    def test_payment_is_displayed(self, driver):
        payment = driver.find_element(By.CSS_SELECTOR, PAYMENT_TEXT)

        assert payment.is_displayed(), "The Payment is not displayed on the page"


    def test_about_us_is_displayed(self, driver):
        about_us = driver.find_element(By.CSS_SELECTOR, ABOUT_US_TEXT)

        assert about_us.is_displayed(), "The About us is not displayed on the page"


    def test_contacts_is_displayed(self, driver):
        driver.find_element(By.CSS_SELECTOR, ABOUT_US_TEXT).click()
        contacts = driver.find_element(By.CSS_SELECTOR, CONTACTS_TEXT)

        assert contacts.is_displayed(), "The Contacts us is not displayed on the page"


    def test_reviews_is_displayed(self, driver):
        reviews = driver.find_element(By.CSS_SELECTOR, REVIEWS_TEXT)

        assert reviews.is_displayed(), "The Reviews is not displayed on the page"


    def test_blog_is_displayed(self, driver):
        blog = driver.find_element(By.CSS_SELECTOR, BLOG_TEXT)

        assert blog.is_displayed(), "The Blog element is not displayed on the page"


    def test_lang_switch_ru_is_displayed(self, driver):
        lang_switch_ru = driver.find_element(By.CSS_SELECTOR, LANG_SWITCH_RU)

        assert (
            lang_switch_ru.is_displayed()
        ), "Russian language switcher is not displayed on the page"


    def test_lang_switch_de_is_displayed(self, driver):
        lang_switch_de = driver.find_element(By.CSS_SELECTOR, LANG_SWITCH_DE)

        assert (
            lang_switch_de.is_displayed()
        ), "German language switcher is not displayed on the page"


    def test_consultation_text_is_displayed(self, driver):
        driver.find_element(By.CSS_SELECTOR, ABOUT_US_TEXT).click()
        driver.find_element(By.CSS_SELECTOR, CONTACTS_TEXT).click()

        driver.find_element(By.CSS_SELECTOR, CALLBACK_BTN).click()
        raw_text = driver.find_element(By.CSS_SELECTOR, CONSULTATION_TEXT).get_attribute(
            "innerText"
        )
        actual_text = " ".join(raw_text.split())

        expected_text = "Запишитесь на бесплатную карьерную консультацию"
        assert (
            actual_text == expected_text
        ), f"Expected text: '{expected_text}', actual text: '{actual_text}'"
