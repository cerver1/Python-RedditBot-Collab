from selenium import webdriver
from time import sleep


def discover_subreddit(driver):
    sleep(2)
    driver.get('https://www.reddit.com/r/random/')
    sleep(5)
    subreddit_name = driver.find_element_by_xpath('//h2[@class="_33aRtz9JtW0dIrBNKFAl0y"]')
    try:
            subscribe = driver.find_element_by_xpath("//button[contains(text(),'Join')]")
            subscribe.click()
            print(f"Succefully subscribed to a new subreddit : {subreddit_name.text}")
    except:
        print(f"We are already subscribed to {subreddit_name.text}")