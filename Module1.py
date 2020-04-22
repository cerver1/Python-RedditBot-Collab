#Log in and returns subreddit names
from selenium import webdriver
import time
import loginInformation

#driver = webdriver.Chrome()
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--disable-notifications")                      #This is to prevent the "Allow notification" dialog box which interferes with the code
#driver = webdriver.Chrome(chrome_options=chrome_options)

def login_subreddit(driver):
    driver.get("https://www.reddit.com/login/")                                 #Opening the login site directly
    #driver.maximize_window()                                
    #time.sleep(10)

    username = loginInformation.login_username
    password = loginInformation.login_password

    time.sleep(2)                                                               #Giving time to load the page


    driver.find_element_by_xpath('/html/body/div/div/div[2]/div/form/div/fieldset[1]/input')\
    .send_keys(username)        #Entering username

    driver.find_element_by_xpath('//*[@id="loginPassword"]')\
    .send_keys(password)                                        #Entering password

    driver.find_element_by_xpath('//button[@class="AnimatedForm__submitButton"]').click()                               #Clicking the logging button

    time.sleep(4)



    #subreddits = driver.find_elements_by_xpath('class="XEkFoehJNxIH9Wlr5Ilzd _2MgAHlPDdKvXiG-Qbz5cbC "')   
    
def subreddit_name_provider(driver):

    open_navigation = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[1]/header/div/div[1]/div[2]/button').click()
    open_navigation

    time.sleep(5)

    subreddits = driver.find_elements_by_xpath('//*[@class="_2aqH0n-kSzFY7HZZ5GL-Jb"]')                                                                                                      

    # leng = len(subreddits)
    # for i in range(5,leng):
    #    print(subreddits[i].text)
    #    subreddit_list= subreddits[i].text

    subreddit_names = []
    for i,subreddit in enumerate(subreddits):
        if i>=5:                                                    #Skipping the subreddit names in favorite section
            subreddit_names.append(subreddit.text)
    
    return subreddit_names
