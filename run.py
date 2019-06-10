import pandas as pd
import csv

url = 'https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv'

data = pd.read_csv(url)

c = data[data.Region == 'SOUTH AMERICA']

(c.Country).to_csv('countries.csv', index=False, header=True)