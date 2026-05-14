import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    options = Options()
    options.add_argument("--start-maximized")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_button_text_change(driver):
    driver.get("http://uitestingplayground.com/textinput")
    wait = WebDriverWait(driver, 5)

    input_field = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input.form-control"))
    )
    input_field.send_keys("ITCH")

    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    assert button.text == "ITCH"


def test_image_loading_alt_attribute(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    wait = WebDriverWait(driver, 15)

    wait.until(EC.text_to_be_present_in_element((By.ID, "text"), "Done!"))
    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")

    third_image_alt = images[2].get_attribute("alt")
    assert third_image_alt == "award", f"Expected 'award', but got '{third_image_alt}'"
