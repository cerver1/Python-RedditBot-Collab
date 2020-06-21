import openpyxl
from Module4 import post_upvote
from selenium import webdriver

"""
Talk to the xlsx database
openpyxl will be exchanged with pandas

"""

wb = openpyxl.load_workbook('reddit_posts.xlsx')
sheet = wb.active

def check_score(post_dict,driver):

    add_data_excel(post_dict,driver)

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
    