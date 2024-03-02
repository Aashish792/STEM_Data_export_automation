from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def download_data(driver, start_date_xpath, end_date_xpath, start_date, end_date, export_button_xpath):
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, start_date_xpath))).send_keys(start_date)
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, end_date_xpath))).send_keys(end_date)
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    
    export_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, export_button_xpath)))
    try:
        export_button.click()
        print("Export Data button clicked successfully.")
    except Exception as e:
        print(f"Error clicking Export Data button: {e}. Attempting alternative method.")
        driver.execute_script("arguments[0].click();", export_button)
        print("Export Data button clicked via JavaScript.")
