from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def login(driver, username, password, stem_center_id):
    username_id = "kc005"
    password_id = "7254AK7254AK"

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, username_id))).send_keys(username)
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, password_id))).send_keys(password)

    stem_center_checkbox = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, stem_center_id)))
    if not stem_center_checkbox.is_selected():
        stem_center_checkbox.click()

    login_button_locator = (By.NAME, "submit")
    button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(login_button_locator))
    driver.execute_script("arguments[0].click();", button)
