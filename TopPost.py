from BrowserControl import browser_close, browserConfig as mainDriver
from Utilities import comment_suffix as cs
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = {'Comments' : [], 'Upvotes' : []}

def convert_str_to_number(x):
    total_stars = 0
    if x == '•':
        total_stars = 0
    elif x == '':
        total_stars = 0
    elif 'k' in x:
        total_stars = float(x.replace('k', '')) * 1000  # convert k to a thousand
    elif 'm' in x:
        total_stars = float(x.replace('m', '')) * 1000000  # convert m to a million
    else:
        total_stars = int(x)  # Less than 1000

    return int(total_stars)

def go_to_subreddit(driver):
    userChoice = input('Please enter a subreddit you would like to visualize [ex: r/subreddit]')

    # add regex to ensure the format is correct
    
    driver.get("https://www.reddit.com/{}".format(userChoice.strip()))

    visualize_posts(driver, userChoice)



def visualize_posts(driver, subreddit_name):

    try:
        print(f"\nPosts from {subreddit_name}")

        top_five_comments = driver.find_elements_by_xpath("//span[@class = 'FHCV02u6Cp2zYL0fhQPsO']")
        top_five_votes = driver.find_elements_by_xpath("//div[@class = '_1rZYMD_4xY3gRcSS3p8ODO']")
        for uv in top_five_votes:
            data['Upvotes'].append(convert_str_to_number(uv.text))
        for c in top_five_comments:
            data['Comments'].append(convert_str_to_number(cs(c.text)))

        df = pd.DataFrame(data)
        df.plot.area(alpha=0.5)
        plt.title("Graph depicting changes in upvotes and comment ratios")
        plt.xlabel("post")
        plt.ylabel("count")
        plt.legend()
        plt.show()

    except:
        print(f"\n Sorry I encountered a problem from {subreddit_name}")
        visualize_posts(driver, userChoice)


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





