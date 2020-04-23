from selenium import webdriver
from time import sleep

"""
log out and close browser

"""

def browser_close(driver):

    sleep(1.5)
    driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[1]/header/div/div[1]/div[2]/button').click()

    user_navigation = driver.find_element_by_xpath('//*[@id ="USER_DROPDOWN_ID"]')
    user_navigation.click()
    
    sleep(1)

    user_logout = driver.find_element_by_xpath('//div[text() = "Log Out"]')
    user_logout.click()

    sleep(1)

    driver.quit()
  