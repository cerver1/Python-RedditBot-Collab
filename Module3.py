from selenium import webdriver
from time import sleep
from Module5 import check_score
from Module4 import post_upvote
from Utilities import remove_prefix

def find_top_posts(driver, subreddit_name):


    print(f"\nPosts from {subreddit_name}")

    top_five_posts = driver.find_elements_by_xpath("//a[@data-click-id = 'body']")[:2]        # returns first 2 posts in the reddit
    # votes = driver.find_elements_by_xpath('//div[@class= "_1rZYMD_4xY3gRcSS3p8ODO"]')         # find all the scores of all the posts on the page
    # post_dict = {}

    got_to_post(driver, top_five_posts)

    # for i in range(2):
                                                                                                
       # post_dict[top_five_posts[i].text] = votes[i].text    # Storing the data in a dictoniary with key as post title and value as upvotes or score
        

def got_to_post(driver, top_five_posts):

    for i in top_five_posts:
        sleep(2)

        trimed_link = remove_prefix(i.get_attribute('href'), 'https://www.reddit.com')
        
        sleep(2)
        
        open_subreddit_post = driver.find_element_by_xpath(f'//a[@data-click-id = "body" and @href = "{trimed_link}"]')
        open_subreddit_post.click()

        post_upvote(driver, trimed_link)

        sleep(2)
        close_subreddit_post = driver.find_element_by_xpath("//button[@title = 'Close']")
        close_subreddit_post.click()


    # links = driver.find_elements_by_tag_name('a')
    # condition = lambda link: 'lake_louise' in link.get_attribute('href')
    # valid_links = list(filter(condition, links))

    sleep(2)

    # provides a list of links from each subreddit
    # check_score(post_dict)            
    # vote_post(driver) 
                              #Calling function which will verify the score of the post and will do the needful 

        
        # posts[i].click()
        # sleep(1)
        # driver.find_elements_by_xpath('//*[@id="overlayScrollContainer"]/div[1]/div/div[2]/button').click()
        # sleep(1)


def go_to_subreddit(driver, subreddit_name):

    xp = f"//span[text()='{subreddit_name}']"
    driver.find_element_by_xpath(xp).click()
    sleep(5)
    find_top_posts(driver, subreddit_name)

    sleep(5)
    driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[1]/header/div/div[1]/div[2]/button').click()

