# openpyxl save
import openpyxl

wb = openpyxl.load_workbook('reddit_posts.xlsx')               #This connected with the excel file
sheet = wb.active          

def check_score(post_dict):

    for keys in post_dict:
        if(post_dict[keys][-1] == "k"):                                                 #This part of program is to remove k from the score variable like '18.2k' 
            post_dict[keys] = float(post_dict[keys][:-1])
            post_dict[keys] = (post_dict[keys] * 1000)                                  #This will change the score to normal integer
        try:
            if(int(post_dict[keys]) > 300):
                print(f"This post have more than 300 votes: {keys}")
                add_data_excel(keys)                                            #Calling function which will verify if the entry is present in excel, if not it will add it
        except ValueError:
            pass

def add_data_excel(post):
    search_row = 0                                       #Will store the row where the entry is found, will be used as a flag variable                                              
    for i in range(1,sheet.max_row + 1):
        if(sheet.cell(row = i,column = 1).value == post):   #Searching if the entry is present in the data or not
            search_row = i
        
    if(search_row == 0):                                                    #If the element is not present in the excel file
        #adding data to excel
        sheet.append([post])                                              #Adding 0 just because append method takes a list of more than 1 value
        wb.save('reddit_posts.xlsx')                                        #Saving the file

        #We can call the upvote function from here since the entry is not present in excel file and the score is greater than 300 or any number

        #upvote_comment(post)            #Remove this comment