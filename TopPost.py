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


# need a method to grab the list of posts on the page - check old reference methods
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
