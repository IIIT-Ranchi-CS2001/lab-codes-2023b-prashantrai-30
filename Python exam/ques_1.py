# load the dataset using pandas and perform
# display first 8 rows
# display last 5 rows
# show the dtype and number of non null values in each column
# use NumPy to compute the mean AQI,maxPM2.5,and min PM10 values for each city
import pandas as pd
import numpy as np

aqi_data = pd.read_csv('AQI_data.csv')
first8rows = aqi_data.head(8)
print("First 8 rows of the dataset:\n", first8rows)
last5rows = aqi_data.tail(5)
print("Last 5 rows of the dataset:\n", last5rows)
datatype = aqi_data.dtypes
print("Data types:\n", datatype)
notnullcount = aqi_data.count()
print("Number of non-null values:\n", notnullcount)
cities = np.unique(aqi_data['City'])
output= np.array([[
    np.mean(aqi_data[aqi_data['City'] == city]['AQI']), 
    np.max(aqi_data[aqi_data['City'] == city]['PM2.5']),  
    np.min(aqi_data[aqi_data['City'] == city]['PM10'])  
] for city in cities])
for city, result in zip(cities, output):
    print(f"City:{city}")
    print(f"Mean AQI: {result[0]:.2f}")
    print(f"Max PM2.5: {result[1]:.2f}")
    print(f"Min PM10: {result[2]:.2f}")
    