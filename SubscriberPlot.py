from selenium import webdriver
from time import sleep
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

def subscriber_plot(driver, subreddit_names):
    
    data = {'Subreddit' : [], 'Subscribers' : [], 'Online' : []}

    for subreddit in subreddit_names:
        url = "http://reddit.com/" + subreddit
        driver.get(url)
        sleep(5)
        element = driver.find_elements_by_class_name("_3XFx6CfPlg-4Usgxm0gK8R")     #Getting subscriber and online count
        subscriber_count = convert_str_to_number(element[0].text)                   #Seprating the subscriber count
        online_count = convert_str_to_number(element[1].text)
        data['Subreddit'].append(subreddit)                                         #Adding data to a dictionary
        data['Subscribers'].append(subscriber_count)
        data['Online'].append(online_count)
        print(f"{subscriber_count} and  {online_count}")
        sleep(5)

    
    df = pd.DataFrame(data)
    subscribers = data['Subscribers']
    online = data['Online']
    print(df)
    x_index = np.arange(len(subreddit_names))
    width = 0.25

    plt.bar(x_index, subscribers, width = width, color="#2738E1", label="Number of Subscribers")
    plt.bar(x_index + 0.25, online, width = width, color="#D9E127", label="Online Subscribers")


    plt.legend()

    plt.xticks(ticks = x_index, labels = subreddit_names)

    plt.title("Graph depicting Subreddits user has subscribed to against Total subscribers and Number of people online")
    plt.xlabel("Subreddits")
    #plt.ylabel("Number")


    plt.tight_layout()
    plt.show()


def convert_str_to_number(x):
    total_stars = 0
    if 'k' in x:
        total_stars = float(x.replace('k', '')) * 1000 # convert k to a thousand
    elif 'm' in x:
        total_stars = float(x.replace('m', '')) * 1000000 # convert m to a million
    else:
        total_stars = int(x) # Less than 1000
    
    return int(total_stars)