from selenium import webdriver
from time import sleep

# This function will receive link of a subreddit and will subscribe to it, if not already done.
def subscribe_to(driver, subreddit_url):
        sleep(5)
        driver.get(subreddit_url)
        sleep(5)
        try:
            subscribe = driver.find_element_by_xpath("//button[contains(text(),'Join')]")
            subscribe.click()
            print("Succefully subscribed to: "+ subreddit_url[22:])
        except:
            print("We are already subscribed to: "+subreddit_url[22:])


# This function will subscribe to top 5 subreddits listed on https://www.reddit.com/r/popular/ if not done already
def follow_popular(driver):
    sleep(5)
    driver.get('http://reddit.com/r/popular')

    sleep(10)

    popular_subreddits = driver.find_elements_by_xpath('//div[@class="_2dr_3pZUCk8KfJ-x0txT_l"]//a[@class="_3ryJoIoycVkA88fy40qNJc"]')

    popular_subreddit_list = []
    j = 0                                                                   # This variable will count number of subreddits already added to the list
    for i in popular_subreddits:
        if i.get_attribute('href') not in popular_subreddit_list:           # To make sure unique subreddit are added
            popular_subreddit_list.append(i.get_attribute('href'))
            j += 1

        if(j>=5):
            break

    #print(popular_subreddit_list)

    for i in popular_subreddit_list: 
        subscribe_to(driver, i)                         


    
