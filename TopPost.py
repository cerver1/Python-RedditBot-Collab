from BrowserControl import browser_close, browserConfig as mainDriver

userChoice = input('Please enter a subreddit you would like to visualize [ex: r/subreddit]')

# add regex to ensure the format is correct

driver = mainDriver()
driver.get("https://www.reddit.com/{}".format(userChoice.strip())) 