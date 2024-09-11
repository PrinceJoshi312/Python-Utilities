from bs4 import BeautifulSoup
import requests
import pandas as pd

url = '' #put your url here to do web scraping

req = requests.get(url)

page = BeautifulSoup(req.text, features='html.parser')

table = page.find_all('table')[0] # specify the index of your table in my case it is 0
titles = table.find_all('th')
table_titles = [title.text.strip() for title in titles]

df = pd.DataFrame(columns = table_titles)
column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data

df.to_csv(r'/Companies.csv', index = False) #put your path where you want to save the csv file also ''' your path here /Companies ''' is the name of the csv file
