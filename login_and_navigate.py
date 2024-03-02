from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from login import login
from navigate import navigate_dropdown, navigate_to_export_page
from datetime import datetime

def login_and_navigate(driver, username, password, stem_center_id, dropdown_id, item_xpath):
    driver.get("https://gannon.mywconline.com/")
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
    login(driver, username, password, stem_center_id)
    navigate_dropdown(driver, dropdown_id)
    navigate_to_export_page(driver, item_xpath)
