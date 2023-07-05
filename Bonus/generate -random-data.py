import random
import csv

# List of years
years = [2019, 2020, 2021, 2022, 2023]

# Generate random cost data
data = []
for year in years:
    for month in range(1, 13):
        cost = random.uniform(100, 1000)  # Generate a random cost value between 100 and 1000
        data.append([year, month, cost])

# Save data to CSV file
filename = 'cost_data.csv'
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Year', 'Month', 'Cost'])
    writer.writerows(data)

print(f"Data saved to {filename}.")
