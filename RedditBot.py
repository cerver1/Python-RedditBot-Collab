# BotBrain

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Module1 import login_subreddit , subreddit_name_provider
from Module2 import browser_close
from Module3 import go_to_subreddit
from Module6 import browserConfig as mainDriver

driver = mainDriver()

login_subreddit(driver)

subreddit_names = subreddit_name_provider(driver)

for i in range((len(subreddit_names))):
  go_to_subreddit(driver, subreddit_names[i])

browser_close(driver)
