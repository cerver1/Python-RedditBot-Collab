from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from LoginControl import login_subreddit , subreddit_name_provider
from BrowserControl import browser_close, browserConfig as mainDriver
from GetPost import go_to_subreddit 
from SubscriberPlot import subscriber_plot
from FollowPopularSubreddits import follow_popular
from DiscoverSubreddit import discover_subreddit

# Open browser
driver = mainDriver()

# Logs you into account 
login_subreddit(driver)

# Gets the names of each subreddit
#subreddit_names = subreddit_name_provider(driver)

'''
# Go to your subreddits
for i in range((len(subreddit_names))):
  go_to_subreddit(driver, subreddit_names[i])
'''

# This function will plot a graph of all subreddits subscribed against number of subscribers and people online
#subscriber_plot(driver, subreddit_names)

# This function will follow top 5 popular subreddits
#follow_popular(driver)

# This function will discover a new randome subreddit and subscribe to it
discover_subreddit(driver)

# Closes down the browser
#browser_close(driver)