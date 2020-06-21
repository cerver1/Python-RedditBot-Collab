from selenium import webdriver
from time import sleep
from Module5 import check_score
from Module4 import post_upvote
from Utilities import remove_prefix

"""

gets top two posts within the subreddit 

"""


def find_top_posts(driver, subreddit_name):


    print(f"\nPosts from {subreddit_name}")

    top_five_posts = driver.find_elements_by_xpath("//a[@data-click-id = 'body']")[:2]
    votes = driver.find_elements_by_xpath('//div[@class= "_1rZYMD_4xY3gRcSS3p8ODO"]')[:2]         # find all the scores of all the posts on the page
  
    got_to_post(driver, top_five_posts, votes)



def got_to_post(driver, top_five_posts, votes):

    post_storage = {}

    for i in top_five_posts:
        sleep(2)
        trimed_link = remove_prefix(i.get_attribute('href'), 'https://www.reddit.com')
        post_storage[trimed_link] = votes[top_five_posts.index(i)].text 
        
        open_subreddit_post = driver.find_element_by_xpath(f'//a[@data-click-id = "body" and @href = "{trimed_link}"]')
        open_subreddit_post.click()

        check_score(post_storage, driver)  # checks if the database contains the link, if so we've already been to that post

        sleep(2)
        close_subreddit_post = driver.find_element_by_xpath("//button[@title = 'Close']")
        close_subreddit_post.click()

    sleep(2)


def go_to_subreddit(driver, subreddit_name):

    xp = f"//span[text()='{subreddit_name}']"
    driver.find_element_by_xpath(xp).click()
    sleep(5)
    find_top_posts(driver, subreddit_name)

    sleep(5)
    driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[1]/header/div/div[1]/div[2]/button').click()

