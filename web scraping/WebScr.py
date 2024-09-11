from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

req = requests.get(url)

page = BeautifulSoup(req.text, features='html.parser')

table = page.find_all('table')[0]
titles = table.find_all('th')
table_titles = [title.text.strip() for title in titles]

df = pd.DataFrame(columns = table_titles)
column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data

df.to_csv(r'C:\Users\HP\OneDrive\Pictures\Companies.csv', index = False)
