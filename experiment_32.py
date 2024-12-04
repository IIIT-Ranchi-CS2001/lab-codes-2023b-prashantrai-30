import numpy as np
import matplotlib.pyplot as plt

# Given data
covid_data = np.array([
    [1500, 2000, 1800, 1200, 900],  # Day 1
    [1600, 2100, 1900, 1300, 950],  # Day 2
    [1700, 2200, 2000, 1400, 1000],  # Day 3
    [1650, 2150, 1950, 1350, 980],   # Day 4
    [1750, 2250, 2050, 1450, 1020],  # Day 5
    [1800, 2300, 2100, 1500, 1050],  # Day 6
    [1900, 2400, 2200, 1600, 1100]   # Day 7
])

countries = ['Country_A', 'Country_B', 'Country_C', 'Country_D', 'Country_E']
days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7']

# Basic Statistics
total_cases_per_country = np.sum(covid_data, axis=0)
max_cases_index = np.argmax(total_cases_per_country)
max_cases_country = countries[max_cases_index]
max_cases = total_cases_per_country[max_cases_index]

print("Basic Statistics:")
for country, total_cases in zip(countries, total_cases_per_country):
    print(f"Total cases in {country}: {total_cases}")
print(f"Country with the highest total cases: {max_cases_country} ({max_cases} cases)")

# Daily Analysis
average_cases_per_day = np.mean(covid_data, axis=1)
total_cases_per_day = np.sum(covid_data, axis=1)
max_cases_day_index = np.argmax(total_cases_per_day)
max_cases_day = days[max_cases_day_index]
max_cases_day_total = total_cases_per_day[max_cases_day_index]

print("\nDaily Analysis:")
for day, avg_cases in zip(days, average_cases_per_day):
    print(f"Average cases on {day}: {avg_cases}")
print(f"Day with the highest total cases: {max_cases_day} ({max_cases_day_total} cases)")

# Trends
percentage_change = ((covid_data[6] - covid_data[0]) / covid_data[0]) * 100
max_percentage_change_index = np.argmax(percentage_change)
max_percentage_change_country = countries[max_percentage_change_index]
max_percentage_change = percentage_change[max_percentage_change_index]

print("\nTrends:")
for country, change in zip(countries, percentage_change):
    print(f"Percentage change for {country} from Day 1 to Day 7: {change:.2f}%")
print(f"Country with the highest percentage increase: {max_percentage_change_country} ({max_percentage_change:.2f}%)")

# Data Transformation (Normalization)
normalized_data = (covid_data - covid_data.min(axis=0)) / (covid_data.max(axis=0) - covid_data.min(axis=0))
