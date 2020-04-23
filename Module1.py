from selenium import webdriver
from time import sleep
import loginInformation

"""

Log into Reddit the account && Return all subreddits 

"""

def login_subreddit(driver):
    
    driver.get("https://www.reddit.com/login/")                                 #Opening the login site directly

    username = loginInformation.login_username
    password = loginInformation.login_password

    sleep(2)                                                               


    username_input = driver.find_element_by_xpath('//*[@id="loginUsername"]')
    username_input.send_keys(username)

    password_input = driver.find_element_by_xpath('//*[@id="loginPassword"]')
    password_input.send_keys(password)                              

    sleep(1)

    login_confirm = driver.find_element_by_xpath('//*[@type="submit"]')
    login_confirm.click()

    sleep(2)

    
def subreddit_name_provider(driver):

    sleep(2)

    subreddit_navigation = driver.find_element_by_xpath('//button[@tabindex=0]')
    subreddit_navigation.click()

    sleep(4)

    subreddit_list = driver.find_elements_by_xpath('//*[@class="_2aqH0n-kSzFY7HZZ5GL-Jb"]')                                                                                                     

    subreddit_names = []
    
    for i,subreddit in enumerate(subreddit_list):
        if i>=5:
            subreddit_names.append(subreddit.text)
    
    return subreddit_names
