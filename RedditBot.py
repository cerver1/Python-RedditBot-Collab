# BotBrain

from selenium import webdriver
from Module1 import login_subreddit
from Module3 import go_to_subreddit

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")                      #This is to prevent the "Allow notification" dialog box which interferes with the code
driver = webdriver.Chrome(chrome_options=chrome_options)

subreddit_names= login_subreddit(driver)


for i in range((len(subreddit_names))):
    go_to_subreddit(driver, subreddit_names[i])