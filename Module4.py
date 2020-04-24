# upvote
from selenium import webdriver
from time import sleep
from Utilities import remove_prefix, comment_list
from random import randint

def post_upvote(driver):
   
    sleep(2)
    
    upvote_button = driver.find_element_by_xpath('//button[@aria-label="upvote"]')
    upvote_status = upvote_button.get_attribute('aria-pressed')
    
    if upvote_status == "false":
        upvote_button.click()

    sleep(2)


# if we are blocked by the site from commenting skip to another post

def post_comment(driver):

    random_index = randint(0,15)
    comment = comment_list[random_index]
    sleep(2)

    comment_box = driver.find_element_by_xpath('//div[@class ="notranslate public-DraftEditor-content"]')
    comment_box.send_keys(comment)
    sleep(4)

    comment_confirm = driver.find_element_by_xpath('//*[@id="overlayScrollContainer"]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/div[3]/div[1]/button')
    comment_confirm.click()
    sleep(2)