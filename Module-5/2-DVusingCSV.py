# Data Visualization using CSV file

# importing required libraries
import pandas as pd
import matplotlib.pyplot as plt

# importing database file (.CSV)
data = pd.read_csv("Module-5\\file.csv")

# checking if the data is available or not.
# print (data)

# Scatter plot with Units against UnitCost
plt.scatter(data['Units'], data['UnitCost'])

# Adding Title to the Plot
plt.title("Scatter Plot")

# Setting the Xlabel and Ylabel
plt.xlabel('Units')
plt.ylabel('UnitCost')

plt.show()