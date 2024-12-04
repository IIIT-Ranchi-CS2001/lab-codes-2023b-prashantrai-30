# using pivot table summarize the dataset where:
# the rows represent the unique city
# the values in the table should be the maximum PM2.5 recorded for each city and save it in a pivot.csv
import pandas as pd
import os

aqi_data = pd.read_csv('AQI_data.csv')
pivot_table = aqi_data.pivot_table(index='City', values='PM2.5', aggfunc='max')
if not os.path.isfile('pivot.csv'):
    pivot_table.to_csv('pivot.csv')
else:
    pivot_table.to_csv('pivot.csv')
