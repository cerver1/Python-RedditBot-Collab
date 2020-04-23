from selenium import webdriver
from time import sleep
from Module5 import check_score
from Module4 import vote_post

def find_top_posts(driver):
    print("\nIn find_top function")
    posts = driver.find_elements_by_xpath('//h3[@class="_eYtD2XCVieq6emjKBH3m"]')           #find all posts on the page
    votes= driver.find_elements_by_xpath('//div[@class= "_1rZYMD_4xY3gRcSS3p8ODO"]')         #find all the scores of all the posts on the page
    post_dict = {}

    for i in range(5):                                                                      #Just storing top 5 posts
        post_dict[posts[i].text] = votes[i].text                                            #Storing the data in a dictoniary with key as post title and value as upvotes or score

    # print(post_dict)
    # check_score(post_dict)            
    vote_post(driver) 
                              #Calling function which will verify the score of the post and will do the needful 

        
        # posts[i].click()
        # sleep(1)
        # driver.find_elements_by_xpath('//*[@id="overlayScrollContainer"]/div[1]/div/div[2]/button').click()
        # sleep(1)


def go_to_subreddit(driver, subreddit_name):

    xp = f"//span[text()='{subreddit_name}']"
    driver.find_element_by_xpath(xp).click()
    sleep(5)
    find_top_posts(driver)

    sleep(5)
    driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[1]/header/div/div[1]/div[2]/button').click()

