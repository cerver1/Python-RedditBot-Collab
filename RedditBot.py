# BotBrain

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Module1 import login_subreddit , subreddit_name_provider
from Module2 import browser_close
from Module3 import go_to_subreddit
from Module6 import browserConfig as mainDriver

# Open browser
driver = mainDriver()

# Logs you into account 
login_subreddit(driver)

# Gets the names of each subreddit
subreddit_names = subreddit_name_provider(driver)

# Go to your subreddits
for i in range((len(subreddit_names))):
  go_to_subreddit(driver, subreddit_names[i])

# Closes down the browser
browser_close(driver)