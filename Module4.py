# upvote
from selenium import webdriver
from time import sleep


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

def vote_post(driver):

    # links = driver.find_elements_by_tag_name('a')
    # condition = lambda link: 'lake_louise' in link.get_attribute('href')
    # valid_links = list(filter(condition, links))
    sleep(2)

    # provides a list of links from each subreddit
    links = driver.find_elements_by_xpath("//a[@data-click-id = 'body']")[:5]

    for i in links:
        sleep(3)
        destination = i.get_attribute('href')
        trimed_res = remove_prefix(destination, 'https://www.reddit.com')
        sleep(2)
        driver.find_element_by_xpath(f'//a[@data-click-id = "body" and @href = "{trimed_res}"]').click()
        # //a[@data-click-id = 'body' and @href = '/r/EarthPorn/comments/g5oqtj/lake_louise_2436x1125_oc/']
        sleep(3)
        close = driver.find_element_by_xpath("//button[@title = 'Close']").click()
        close

        print(destination)
    
    #






'''
Remove this comment 

def upvote_comment(post):

    #This is the only function remaining 
    #I think we will have to send the driver too in this function but since this function is being called from module 5 where we havent send the driver yet
    #so after you write this module and it doesnt work try sending the driver to first module 5 and then to this function to make it work
    # 
    # To open the post for commenting on it you can use the following xpaths
    # 
    # open_post_xpath = "//h3[text() = post]"
    #  
    # So now the tasks which are remaing are : 
    # 1. Open the post
    # 2. Enter something in the text box
    # 3. Press the comment button
    # 4. Click on the upvote button
    # 5.Get some comments from the post and print it in cmd 
    #
    #
    #
    #



'''