from bs4 import BeautifulSoup 
import requests


url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

page = requests.get(url)

# print(page)  if 200 wich means the web page allows to do the scrapping

html_page = BeautifulSoup(page.text , 'html')

table = html_page.find('table' , class_ = 'wikitable sortable')

world_titles = table.find_all('th')

world_table_titles = [title.text.strip() for title in world_titles]

import pandas as pd

df = pd.DataFrame(columns= world_table_titles)

columns_data = table.find_all('tr') # find all the rows


for row in columns_data[1:]:
    row_data = row.find_all('td') # for each row search for all columns 
    individual_row_data = [data.text.strip() for data in row_data] #list of data of the all row

    length = len(df)
    df.loc[length] = individual_row_data #insert the row data to end of dataframe

print(df)


df.to_csv(r'C:\Users\hhafs\OneDrive\Bureau\Data analyst\Python\companies.csv' , index = False)