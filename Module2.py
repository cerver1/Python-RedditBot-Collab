# log out and close browser
from selenium import webdriver
from time import sleep

# log out

def browser_close(driver):

    # without the website call below an exception is thrown
    #driver.get('https://www.reddit.com/')

    sleep(1.5)
    driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[1]/header/div/div[1]/div[2]/button').click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/header/div/div[2]/div[2]/div/div[2]/button').click()
    
    sleep(1)

    driver.find_element_by_xpath('//div[text() = "Log Out"]').click()
    

    sleep(1)

    driver.quit()
    # driver.get()
  