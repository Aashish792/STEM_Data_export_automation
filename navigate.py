from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def navigate_dropdown(driver, dropdown_id):
    dropdown_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, dropdown_id)))
    driver.execute_script("arguments[0].click();", dropdown_element)

def navigate_to_export_page(driver, item_xpath):
    item_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, item_xpath)))
    item_element.click()
