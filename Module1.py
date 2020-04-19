# open browser and log in
from selenium import webdriver
import time

#driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")                      #This is to prevent the "Allow notification" dialog box which interferes with the code
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://www.reddit.com/login/")                                 #Opening the login site directly
driver.maximize_window()                                
#time.sleep(10)

f=open("loginInformation.py","r")                                           #Reading username and passwords                    
lines=f.readlines()
username=lines[4].split('"')[1]                                                 
password=lines[5].split('"')[1]
f.close()

time.sleep(2)                                                               #Giving time to load the page


driver.find_element_by_xpath('/html/body/div/div/div[2]/div/form/div/fieldset[1]/input').send_keys(username)        #Entering username

driver.find_element_by_xpath('//*[@id="loginPassword"]').send_keys(password)                                        #Entering password

driver.find_element_by_xpath('//button[@class="AnimatedForm__submitButton"]').click()                               #Clicking the logging button

time.sleep(10)                                                                                                      #Giving time to user to see before the brower closes

driver.close()