from selenium import webdriver
from time import sleep
from Module5 import check_score
from Module4 import vote_post
from Utilities import remove_prefix

def find_top_posts(driver, subreddit_name):


    print(f"\nPosts from {subreddit_name}")

    top_five_posts = driver.find_elements_by_xpath("//a[@data-click-id = 'body']")[:2]        # find all posts on the page
    votes = driver.find_elements_by_xpath('//div[@class= "_1rZYMD_4xY3gRcSS3p8ODO"]')         # find all the scores of all the posts on the page
    post_dict = {}

    for i in range(2):
                                                                              # Just storing top 5 posts                                       # Storing the data in a dictoniary with key as post title and value as upvotes or score
        post_dict[top_five_posts[i].text] = votes[i].text  
        

    print(post_dict)

    # links = driver.find_elements_by_tag_name('a')
    # condition = lambda link: 'lake_louise' in link.get_attribute('href')
    # valid_links = list(filter(condition, links))

    sleep(2)

    # provides a list of links from each subreddit
    
'''
    for i in top_five_posts:
        sleep(3)
        destination = i.get_attribute('href')
        trimed_res = remove_prefix(destination, 'https://www.reddit.com')
        sleep(2)
        driver.find_element_by_xpath(f'//a[@data-click-id = "body" and @href = "{trimed_res}"]').click()

        post_upvote(driver) # upvote
        post_comment(driver) # comment


        sleep(2)
        close = driver.find_element_by_xpath("//button[@title = 'Close']").click()
        close

        print(destination)

'''
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

