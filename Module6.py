from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def browserConfig():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    return driver