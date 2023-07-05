import matplotlib.pyplot as plt

# Data for the pie chart
languages = ['Python', 'JavaScript', 'Java', 'C++', 'C#']

# Percentages for each language
popularity = [30, 25, 20, 15, 10]  

# Create the pie chart
plt.pie(popularity, labels=languages, autopct='%1.1f%%')

# Add a title
plt.title('Trending Programming Languages')

# Display the chart
plt.show()
