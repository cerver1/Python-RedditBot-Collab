import openpyxl
from Module4 import post_upvote
from selenium import webdriver

wb = openpyxl.load_workbook('reddit_posts.xlsx')               #This connected with the excel file
sheet = wb.active

def check_score(post_dict,driver):

    add_data_excel(post_dict,driver)

#    for keys in post_dict:
#        if(post_dict[keys][-1] == "k"):                                                 #This part of program is to remove k from the score variable like '18.2k' 
#            post_dict[keys] = float(post_dict[keys][:-1])
#            post_dict[keys] = (post_dict[keys] * 1000)                                  #This will change the score to normal integer
#        try:
#            add_data_excel(keys, driver)                                            #Calling function which will verify if the entry is present in excel, if not it will add it
#        except ValueError:
#            pass

"""
fix the dictionary result in Module 3
"""
def add_data_excel(post_dict,driver):
    
    list_of_saved_links = []

    for i in sheet['A']:
        list_of_saved_links.append(i.value)
    
    for key in post_dict:
        if key in list_of_saved_links:
            print("This post already exists")
        else:
            sheet.append([key])
            post_upvote(driver)
            wb.save('reddit_posts.xlsx') 
            print("This is a new post!")
    