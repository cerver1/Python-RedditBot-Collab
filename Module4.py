# upvote
from selenium import webdriver
from time import sleep
from Utilities import remove_prefix

def post_upvote(driver,trimed_link):
    # upvotes each post
    # condition to downvote needs to be added
    sleep(2)
    
    upvote_button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[3]/div/div/div/div[1]/div/div[1]/div[1]/button[1]')
    upvote_status = upvote_button.get_attribute('aria-pressed')
    # regex needed of the post link, to join it to the upvote id
    if str(upvote_status) == "false":
        upvote_button.click
    else:
        print(trimed_link)

    sleep(2)


# if we are blocked by the site from commenting skip to another post

def post_comment(driver):

    sleep(2)
    driver.find_element_by_xpath('//div[@class ="notranslate public-DraftEditor-content"]')\
    .send_keys("Beautiful!!") # comment
    sleep(4)
    driver.find_element_by_xpath('//*[@id="overlayScrollContainer"]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/div[3]/div[1]/button').click() # confirm comment
   

    sleep(2)