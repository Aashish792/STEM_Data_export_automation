import sys
from initialize_driver import initialize_driver
from login_and_navigate import login_and_navigate
from download_data import download_data
from file_operations import move_file
from datetime import datetime
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 main.py <username> <password>")
        return

    username = sys.argv[1]
    password = sys.argv[2]

    driver = initialize_driver()

    stem_center_id = "sc65a187887bdc1"
    dropdown_id = "optionsDropdown"
    item_xpath = '//*[@id="navbarSupportedContent"]/ul/li[1]/ul/li[15]/a'

    login_and_navigate(driver, username, password, stem_center_id, dropdown_id, item_xpath)

    start_date_xpath = '//*[@id="e_start"]'
    end_date_xpath = '//*[@id="e_end"]'
    start_date = "01/02/2023"
    end_date = datetime.now().strftime("%m/%d/%Y")
    export_button_xpath = '/html/body/main/div/div[1]/div/form/p[2]/button'

    download_data(driver, start_date_xpath, end_date_xpath, start_date, end_date, export_button_xpath)

    download_dir = "/Users/aashish/Downloads"
    filename_pattern = "Appointments.Starting"
    destination_dir = "/Users/aashish/Desktop"

    timeout = 120
    end_time = time.time() + timeout
    while time.time() < end_time:
        for fname in os.listdir(download_dir):
            if fname.startswith(filename_pattern):
                file_path = os.path.join(download_dir, fname)
                break
        if file_path:
            print(f"File downloaded to {file_path}")
            break
        else:
            time.sleep(1)

    if not file_path:
        print("Download timed out or file not found.")

    move_file(download_dir, destination_dir, filename_pattern)

    print("Completed!!")
    driver.quit()

if __name__ == "__main__":
    main()
