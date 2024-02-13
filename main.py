from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

print("Starting Website")
driver = webdriver.Chrome(options=options)
driver.get("https://gannon.mywconline.com/")
sleep(3)


# Login using credentials.
username = "test"
password = "test"
username_id = "username"  
password_id = "password"  
stem_center_id = "sc65a187887bdc1"  
login_button = driver.find_element(By.NAME, "submit")

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, username_id))).send_keys(username)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, password_id))).send_keys(password)

# Check the STEM Center box if not already checked.
stem_center_checkbox = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, stem_center_id)))
if not stem_center_checkbox.is_selected():
    stem_center_checkbox.click()

# Click the Log In button.
login_button.click()
print("login sucessful")
# Assuming there's some loading time after login
sleep(10)


## TODO: Worl on the second part

# Your code for what to do after login goes here
# Close the driver
# driver.quit()
