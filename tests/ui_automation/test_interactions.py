import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    def _accept_cookies():
        try:
            wait = WebDriverWait(driver, 5)
            cookie_button = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'button[class="fc-button fc-cta-consent fc-primary-button"]')))
            cookie_button.click()
        except TimeoutException:
            pass

    driver.accept_cookies = _accept_cookies

    yield driver
    driver.quit()


def test_iframes(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    wait = WebDriverWait(driver, 10)

    iframe = wait.until(
        EC.presence_of_element_located((By.ID, "my-iframe"))
    )

    driver.switch_to.frame(iframe)

    target_text = "semper posuere integer et senectus justo curabitur."

    element = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, f"//*[contains(normalize-space(.), '{target_text}')]")
        )
    )

    assert element.is_displayed()
    driver.switch_to.default_content()


def test_drag_and_drop(driver):
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    wait = WebDriverWait(driver, 10)
    driver.accept_cookies()

    demo_frame = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "demo-frame")))
    driver.switch_to.frame(demo_frame)

    gallery_items = driver.find_elements(By.CSS_SELECTOR, "#gallery li")
    trash_area = driver.find_element(By.ID, "trash")

    first_image = gallery_items[0]

    actions = ActionChains(driver)
    actions.drag_and_drop(first_image, trash_area).perform()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#trash li")))

    trash_count = len(driver.find_elements(By.CSS_SELECTOR, "#trash li"))
    gallery_count = len(driver.find_elements(By.CSS_SELECTOR, "#gallery li"))

    assert trash_count == 1, f"Expected 1 image in trash, but found {trash_count}"
    assert gallery_count == 3, f"Expected 3 images in gallery, but found {gallery_count}"