import matplotlib.pyplot as plt

# Data for the pie chart
languages = ['Python', 'JavaScript', 'Java', 'C++', 'C#']
popularity = [30, 25, 20, 15, 10]  # Percentages for each language
explode = [0.1, 0.1, 0.1, 0.1, 0.1]  # Explode the first slice

# Create the pie chart
plt.pie(popularity, labels=languages, explode=explode, autopct='%1.1f%%')

# Add a title
plt.title('Trending Programming Languages')

# Display the chart
plt.show()
