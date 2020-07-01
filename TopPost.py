from BrowserControl import browser_close, browserConfig as mainDriver
from Utilities import comment_suffix as cs


def convert_str_to_number(x):
    total_stars = 0
    if 'k' in x:
        total_stars = float(x.replace('k', '')) * 1000  # convert k to a thousand
    elif 'm' in x:
        total_stars = float(x.replace('m', '')) * 1000000  # convert m to a million
    else:
        total_stars = int(x)  # Less than 1000

    return int(total_stars)


userChoice = input('Please enter a subreddit you would like to visualize [ex: r/subreddit]')

# add regex to ensure the format is correct

driver = mainDriver()
driver.get("https://www.reddit.com/{}".format(userChoice.strip()))

def find_top_posts(driver, subreddit_name):

    print(f"\nPosts from {subreddit_name}")

    top_five_posts = driver.find_elements_by_xpath("//a[@data-click-id = 'body']//parent::div//parent::div//parent::div[@data-click-id= 'background']//span[@class = 'FHCV02u6Cp2zYL0fhQPsO'")[:5]
    top_five_comments = driver.find_elements_by_xpath("//a[@data-click-id = 'body']//parent::div//parent::div//parent::div[@data-click-id= 'background']//span[@class = 'FHCV02u6Cp2zYL0fhQPsO']")[:]
    
    top_five_votes = driver.find_elements_by_xpath("//a[@data-click-id = 'body']//parent::div//parent::div//parent::div[@data-click-id= 'background']//preceding-sibling::div//div//div[@class = '_1rZYMD_4xY3gRcSS3p8ODO']")
  
    
    for post in top_five_posts:
        vote = post.get_attribute(top_five_votes).text
        comment = post.get_attribute(top_five_comments[top_five_posts.index(post)]).text
        data = {post.get_attribute('href') : (comment, vote)}
        print(data)
        # driver.find_elements_by_xpath("//div[@class = '_1E9mcoVn4MYnuBQSVDt1gC']//div[@class = '_1rZYMD_4xY3gRcSS3p8ODO']")

        # driver.find_elements_by_xpath("//span[@class = 'FHCV02u6Cp2zYL0fhQPsO']")

find_top_posts(driver, userChoice)

def get_upvote_comment():
    try:

        upvote_element = driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[4]/div[1]/div/div/div[1]/div/div')

        upvote_count = convert_str_to_number(upvote_element[0].text)  # Seprating the subscriber count

        comment_element = driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[4]/div[2]/div/div/div[2]/div[4]/div[2]/a/span')

        comment_count = cs(upvote_element[0].text)
    except:
        return 'Unable to grab the the values from this post'

    return upvote_count, comment_count


'''
vote = get_upvote_comment()

print(vote[0])
print(vote[1])
'''