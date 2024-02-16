from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from datetime import datetime
import os
import time
import shutil



options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

print("Starting Website")
driver = webdriver.Chrome(options=options)
driver.get("https://gannon.mywconline.com/")
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "body")))  # Wait for page to load

# Login using credentials.
username = "test"
password = "test"
username_id = "username"
password_id = "password"
stem_center_id = "sc65a187887bdc1"

WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, username_id))).send_keys(username)
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, password_id))).send_keys(password)

stem_center_checkbox = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, stem_center_id)))
if not stem_center_checkbox.is_selected():
    stem_center_checkbox.click()
    
# Locate the login button
login_button_locator = (By.NAME, "submit")
button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(login_button_locator))

# Use JavaScript to click
driver.execute_script("arguments[0].click();", button)

print("Login attempt made")

# Adjusting wait time to ensure the page has loaded after login attempt
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
#Open dropdown after login

dropdown_id = "optionsDropdown"
dropdown_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, dropdown_id)))
driver.execute_script("arguments[0].click();", dropdown_element)

#Click on System data export after the dropdown

item_xpath = '//*[@id="navbarSupportedContent"]/ul/li[1]/ul/li[15]/a'
item_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, item_xpath)))
item_element.click()

sleep(5)

# Set the start and end dates
start_date_xpath = '//*[@id="e_start"]'
end_date_xpath = '//*[@id="e_end"]'
start_date = "01/02/2023"
end_date = datetime.now().strftime("%m/%d/%Y")  # Format today's date as MM/DD/YYYY

WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, start_date_xpath))).send_keys(start_date)
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, end_date_xpath))).send_keys(end_date)

# Wait for any dynamic page updates that might occur after date selection
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Locate the "Export Data" button using its XPath and attempt to click
export_button_xpath = '/html/body/main/div/div[1]/div/form/p[2]/button'
export_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, export_button_xpath)))

try:
    export_button.click()
    print("Export Data button clicked successfully.")
except Exception as e:
    print(f"Error clicking Export Data button: {e}. Attempting alternative method.")
    driver.execute_script("arguments[0].click();", export_button)
    print("Export Data button clicked via JavaScript.")

# Assuming the filename you expect, adjust the pattern as needed
download_dir = "/Users/aashish/Downloads"
filename_pattern = "Appointments.Starting"  # This should be part of your expected file name
destination_dir = "/Users/aashish/Desktop"
file_path = "/Users/aashish/Downloads"

#

def move_file(src_directory, dst_directory, pattern):
    for fname in os.listdir(src_directory):
        if fname.startswith(pattern):
            src_path = os.path.join(src_directory, fname)
            dst_path = os.path.join(dst_directory, fname)
            shutil.move(src_path, dst_path)
            print(f"File moved to {dst_path}")
            return dst_path
    return None

# Wait for the download to complete with a timeout
timeout = 120  # seconds
end_time = time.time() + timeout
while time.time() < end_time:
    for fname in os.listdir(download_dir):
        if fname.startswith(filename_pattern):
            file_path = os.path.join(download_dir, fname)
            break
    if file_path:
        print(f"File downloaded to {file_path}")
        print("Completed!!!!!!!!!!!!!")
        break
    else:
        time.sleep(1)  # Check every second

if not file_path:
    print("Download timed out or file not found.")
    
sleep(5)    

move_file(download_dir, destination_dir, filename_pattern)

sleep(5)

print("Completed!!")
# Close the driver after finishing
driver.quit()
