# upvote
from selenium import webdriver
from time import sleep
from Utilities import remove_prefix, comment_list
from random import randint


"""
upvote and downvote selected posts

"""

def post_upvote(driver):
   
    sleep(1.5)
    upvote_button = driver.find_element_by_xpath('//div[@class = "_1rZYMD_4xY3gRcSS3p8ODO"]//preceding-sibling::button')
    sleep(0.5)
    upvote_status = upvote_button.get_attribute('aria-pressed')
    
    try:

        if upvote_status == "false":
            sleep(0.5)
            upvote_button.click()
    except: 
        print('unable to upvote this post')

    sleep(2)


def post_downvote(driver):
   
    sleep(1.5)
    downvote_button = driver.find_element_by_xpath(' //div[@class = "_1rZYMD_4xY3gRcSS3p8ODO"]//following-sibling::button')
    sleep(0.5)
    downvote_status = downvote_button.get_attribute('aria-pressed')
    
    try:

        if downvote_status == "false":
            sleep(0.5)
            downvote_button.click()
    except: 
        print('unable to upvote this post')

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