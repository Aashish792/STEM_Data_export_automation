from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def initialize_driver():
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    return webdriver.Chrome(options=options)
